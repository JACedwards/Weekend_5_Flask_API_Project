from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

from app.models import Animal

@api.route("/test", methods=['GET'])
def test():
    fox = Animal.query.all()[0]
    return jsonify(fox.to_dict()), 200

@api.route('/animals', methods = ['GET'])
def getAnimals():
    """
    GET retrieves all animals from our database and returns them as JSON data
    """
    animals = Animal.query.all()
    # animals = [a.to_dict() for a in animals]  list  version
    animals = {a.species: a.to_dict() for  a in animals}  #dictionary version in comprehension form

    return jsonify(animals), 200

