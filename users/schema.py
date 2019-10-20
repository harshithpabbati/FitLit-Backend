import graphene
from .models import Profile
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from graphql_jwt.decorators import login_required


class ProfileObj(graphene.ObjectType):
    username = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    weight = graphene.Decimal()
    height = graphene.Decimal()
    age = graphene.Int()

    def resolve_username(self, info):
        user = User.objects.get(id=self['user_id'])
        return user.username

    def resolve_firstName(self, info):
        user = User.objects.get(id=self['user_id'])
        return user.first_name

    def resolve_lastName(self, info):
        user = User.objects.get(id=self['user_id'])
        return user.last_name

    def resolve_age(self, info):
        diff = date.today() - self['dob']
        return diff.total_seconds() / timedelta(days=365).total_seconds()


class Query(object):
    profile = graphene.Field(ProfileObj)

    @login_required
    def resolve_profile(self, info, **kwargs):
        profile = Profile.objects.values().get(user=info.context.user)
        return profile