import json

from django.contrib.auth import get_user_model

from channels import Group
from channels.auth import channel_session_user
from channels.sessions import channel_session

from apps.chat.models import Room, Message, UserRoom


User = get_user_model()


@channel_session_user
def ws_chat_connect(message):
    try:
        message.reply_channel.send({'accept': True})
        label = message['path'].split('/')[2]
        room = Room.objects.get(label=label)
        Group('chat-' + label, channel_layer=message.channel_layer).add(message.reply_channel)
        message.channel_session['room'] = label
    except (KeyError, Room.DoesNotExist):
        pass


@channel_session_user
def ws_chat_receive(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except (KeyError, Room.DoesNotExist):
        return

    try:
        data = json.loads(message['text'])
    except ValueError:
        return

    if data:
        try:
            user = User.objects.get(username=data['user'])
            room_message = room.messages.create(user=user, message=data['message'])
            Group('chat-' + label, channel_layer=message.channel_layer).send(
                {
                    'text': json.dumps(
                        {
                            'user': room_message.user.username,
                            'message': room_message.message,
                            'timestamp': room_message.formatted_timestamp,
                        })
                })
        except (KeyError, User.DoesNotExist, ValueError):
            return


@channel_session_user
def ws_chat_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('chat-' + label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        return
