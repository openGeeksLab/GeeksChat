import json

from django.conf import settings
from django.contrib.auth import get_user_model

from channels import Group
from channels.auth import channel_session_user
from channels.sessions import channel_session
from push_notifications.models import APNSDevice, GCMDevice

from apps.chat.models import Room, Message, UserRoom
from apps.chat.utils import catch_ws_error, get_room_or_error, get_user_or_error


User = get_user_model()


@channel_session_user
@catch_ws_error
def ws_chat_connect(message):
    message.reply_channel.send({"accept": True})
    label = message['path'].split('/')[2]
    room = get_room_or_error(label, message.user)
    room.websocket_group.add(message.reply_channel)
    message.channel_session['room'] = label


@channel_session_user
@catch_ws_error
def ws_chat_receive(message):
    label = message.channel_session['room']
    room = get_room_or_error(label, message.user)
    data = json.loads(message['text'])

    if data:
        user = get_user_or_error(data['user'])
        room_message = room.messages.create(user=user, message=data['message'])
        room.websocket_group.send(
            {
                'text': json.dumps(
                    {
                        'user': room_message.user.username,
                        'message': room_message.message,
                        'timestamp': room_message.formatted_timestamp,
                    })
            })


@channel_session_user
@catch_ws_error
def ws_chat_disconnect(message):
    label = message.channel_session['room']
    room = get_room_or_error(label, message.user)
    room.websocket_group.discard(message.reply_channel)
