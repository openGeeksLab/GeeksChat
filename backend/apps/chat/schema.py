from django.contrib.auth import get_user_model

import django_filters
from graphene import relay, ObjectType, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.chat.models import Room, Message, UserRoom


User = get_user_model()


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)


class RoomNode(DjangoObjectType):

    class Meta:
        model = Room
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'label': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)


class MessageNode(DjangoObjectType):

    class Meta:
        model = Message
        filter_fields = {
            'room': ['exact'],
            'user': ['exact'],
            'message': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)


class UserRoomNode(DjangoObjectType):

    class Meta:
        model = UserRoom
        filter_fields = {
            'room': ['exact'],
            'user': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    room = relay.Node.Field(RoomNode)
    all_rooms = DjangoFilterConnectionField(RoomNode)

    message = relay.Node.Field(MessageNode)
    all_messages = DjangoFilterConnectionField(MessageNode)

    user_room = relay.Node.Field(UserRoomNode)
    all_user_rooms = DjangoFilterConnectionField(UserRoomNode)

    class Meta:
        abstract = True
