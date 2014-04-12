from flask import Flask, current_app
from uuid import uuid4

class API(object):

    def state(self, req):
        if req.method == 'POST':
            guid = uuid4()
            current_app.redis_store.set(guid, 'stuff')
            return {'id': guid}
