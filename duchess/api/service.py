from flask import current_app as duchess
from uuid import uuid4


class API(object):

    def state(self, req):
        if req.method == 'POST':
            guid = uuid4()
            duchess.redis.set(guid, 'stuff')
            return {'id': guid}

    def slides(self, req):
        if req.method == 'POST':
            duchess.redis.set(
                'slide:' + req.form['id'] + ':text', req.form['text']
            )
            duchess.redis.set(
                'slide:' + req.form['id'] + ':image', req.form['image']
            )
            return {'random_id': str(uuid4())[4:13]}
