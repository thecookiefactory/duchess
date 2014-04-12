from flask import Blueprint, jsonify, request
from duchess.api.service import API

api_router = Blueprint('api_router', __name__)
duchess_api = API()


@api_router.route('/api/<endpoint>')
def call_api(endpoint):
    return jsonify(getattr(duchess_api, endpoint)(request))
