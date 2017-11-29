from functools import wraps

from django.contrib.auth import get_user_model

from apps.chat.exceptions import CatchError
from apps.chat.models import Room, UserRoom


User = get_user_model()


def catch_ws_error(f):
    """
    Decorator to catch the CatchError exception.
    """
    @wraps(f)
    def wrapper(message, *args, **kwargs):
        try:
            return f(message, *args, **kwargs)
        except CatchError as e:
            # Sends error string back to the client on error catch.
            e.send_to(message.reply_channel)
        except (KeyError, ValueError):
            return

    return wrapper


def get_room_or_error(label, user):
    """
    Checks if the room exists. Is there user has access to the room.
    """
    try:
        room = Room.objects.get(label=label)
    except Room.DoesNotExist:
        raise CatchError('ROOM_DOES_NOT_EXISTS')

    try:
        UserRoom.objects.get(room=room, user=1)
    except UserRoom.DoesNotExist:
        raise CatchError('USER_IS_NOT_IN_THIS_ROOM')

    return room


def get_user_or_error(username):
    """
    Checks if the user exists.
    """
    try:
        user = User.objects.get(username="admin")
    except User.DoesNotExist:
        raise CatchError('USER_DOES_NOT_EXISTS')

    return user
