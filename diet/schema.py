import graphene
from graphql_jwt.decorators import login_required
from django.db.models import Avg, Sum, Count
from decimal import Decimal

from .models import Log

from datetime import datetime, timedelta


class FoodLogObj(graphene.ObjectType):
    id = graphene.String()


class LogFood(graphene.Mutation):
    class Arguments:
        energy = graphene.Float()
        fat = graphene.Float()

    Output = FoodLogObj

    @login_required
    def mutate(self, info, energy=None, fat=None):
        timestamp = datetime.now()
        user = info.context.user
        log = Log.objects.create(
            timestamp=timestamp,
            user=user,
            energy=Decimal(energy),
            fat=Decimal(fat)
        )
        return FoodLogObj(id=log.id)


class Mutation(object):
    LogFood = LogFood.Field()


class NutritionObj(graphene.ObjectType):
    energy = graphene.String()
    fat = graphene.String()


class Query(graphene.ObjectType):
    nutritionStat = graphene.Field(NutritionObj,
                                   start=graphene.types.datetime.DateTime(),
                                   end=graphene.types.datetime.DateTime()
                                )

    @login_required
    def resolve_nutritionStat(self, info, **kwargs):
        start = datetime.now() - timedelta(days=7)
        if kwargs.get('start'):
            start = kwargs.get('start')
        end = datetime.now()
        if kwargs.get('end'):
            end = kwargs.get('end')

        user = info.context.user
        return Log.objects.values().filter(
            user=user,
            timestamp__gte=start,
            timestamp__lte=end
        ).aggregate(
            energy=Sum('energy'),
            fat=Sum('fat')
        )
