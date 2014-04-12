from flask import current_app as duchess
from uuid import uuid4


class API(object):

    def state(self, req):
        if req.method == 'POST':
            guid = uuid4()
            duchess.redis_store.set(guid, 'stuff')
            return {'id': guid}
