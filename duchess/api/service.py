from flask import Flask
import uuid
import duchess

class API(object):

    def state(self, req):
        if req.method == 'GET':
            guid = uuid.uuid4()
            duchess.redis_store.set(guid, 'stuff')
            return {'id': guid}
        elif req.method == 'POST':
            guid = uuid.uuid4()
            duchess.redis_store.set(guid, 'stuff')
            return {'id': guid}
