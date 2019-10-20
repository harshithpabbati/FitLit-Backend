import graphene
import graphql_jwt
import requests
from google.cloud import vision
from users.schema import Query as usersQuery
from framework.settings import EDMAM_APP_ID, EDMAM_APP_KEY


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class PredictionObj(graphene.ObjectType):
    name = graphene.String()
    score = graphene.String()

    def resolve_name(self, info):
        return self.description


class PredictionData(graphene.ObjectType):
    dishes = graphene.List(PredictionObj)

    def resolve_labels(self, info):
        list = []
        common = ['Dish', 'Cuisine', 'Fried food', 'Food', 'Ingredient', 'Breakfast', 'Produce']
        for item in self.label_annotations:
            if item.description not in common:
                list.append(item)
        return list


class NutrientObj(graphene.ObjectType):
    nutrient = graphene.String()
    value = graphene.String()

    def resolve_nutrient(self, info):
        return self[0]

    def resolve_value(self, info):
        return self[1]


class FoodItemObj(graphene.ObjectType):
    name = graphene.String()
    nutrients = graphene.List(NutrientObj)

    def resolve_name(self, info):
        return self['food']['label']

    def resolve_nutrients(self, info):
        list = []
        for key, value in self['food']['nutrients'].items():
            temp = [key, value]
            list.append(temp)
        return list


class Query(usersQuery, graphene.ObjectType):
    identifyFood = graphene.Field(PredictionData, image=graphene.String(required=True))
    searchNutrient = graphene.List(FoodItemObj, query=graphene.String(required=True))

    def resolve_identifyFood(self, info, **kwargs):
        imageURL = kwargs.get("image")
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = imageURL

        return client.label_detection(image=image)

    def resolve_searchNutrient(self, info, **kwargs):
        query = kwargs.get('query')
        URL = 'https://api.edamam.com/api/food-database/parser'
        PARAMS = {
            'app_key': EDMAM_APP_KEY,
            'app_id': EDMAM_APP_ID,
            'ingr': query
        }
        response = requests.get(url=URL, params=PARAMS).json()
        return response['hints']


schema = graphene.Schema(mutation=Mutation, query=Query)