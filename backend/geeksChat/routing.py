from channels import route

from apps.chat.consumers import ws_chat_connect, ws_chat_receive, ws_chat_disconnect


channel_routing = [
    route('websocket.connect', ws_chat_connect, path=r'^/chat/'),
    route('websocket.receive', ws_chat_receive, path=r'^/chat/'),
    route('websocket.disconnect', ws_chat_disconnect, path=r'^/chat/'),
]
