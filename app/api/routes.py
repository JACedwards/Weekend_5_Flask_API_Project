from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

from app.models import Animal

@api.route("/test", methods=['GET'])
def test():

    return jsonify('testing some data'), 200