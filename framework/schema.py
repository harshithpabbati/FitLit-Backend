import graphene
import graphql_jwt
from users.schema import Query as usersQuery


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(usersQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)