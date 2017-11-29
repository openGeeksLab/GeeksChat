import json


class CatchError(Exception):
    """
    On error on channels sends error back to the client.
    """
    def __init__(self, code):
        super(CatchError, self).__init__(code)
        self.code = code

    def send_to(self, channel):
        channel.send({
            'text': json.dumps({
                'error': self.code,
            }),
        })
