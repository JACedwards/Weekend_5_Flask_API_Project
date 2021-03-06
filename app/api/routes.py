from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')

from app.models import Animal,db

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

@api.route('/animal/<string:name>', methods=['GET'])
def getAnimalName(name):

    print(name)
    animal = Animal.query.filter_by(species=name.title()).first()
    if animal:
        return jsonify(animal.to_dict()), 200

    return jsonify({'error': f"no such animal with the name: {name.title()}"})


api.route('/create', methods=['POST'])
# @token_required
def createAnimal():
    '''
    [POST] create a new animal in our database with data provided in the request body
    expected data format: JSON:
        {
            'species': <str>,
            'description': <str>,
            'price': <numeric>,
            # all other K:V pairs optional
            'latin_name': <str>,
            'image': <str>,
            'size_cm': <int>,
            'diet': <str>,
            'lifespan':<str>
        }
    '''
    try:

        newdict = request.get_json()
        print(newdict)
        a = Animal(newdict)
        print(a)
    except:
        return jsonify({'error': 'improper request or body data'}), 400
    try:
        db.session.add(a)
        db.session.commit()
    except:
        return jsonify({'error': 'species already exists in the database'}), 400
    # and tell our user that the operation was successful
    return jsonify({'created': a.to_dict()}), 200

@api.route('/update/<string:id>', methods=['POST'])
# @token_required
def updateAnimal(id):
    '''
    [POST] updates an existing animal in our database with data provided in the request body
    expected data format: JSON:
        {
            # ALL K:V pairs optional, must have at least one
            'species': <str>,
            'description': <str>,
            'price': <numeric>,
            'latin_name': <str>,
            'image': <str>,
            'size_cm': <int>,
            'diet': <str>,
            'lifespan':<str>
        }
    '''
    try:
        newvals = request.get_json()
        animal = Animal.query.get(id)
        animal.from_dict(newvals)
        db.session.commit()
        return jsonify({'Updated animal': animal.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'Invalid request or animal ID does not exist.'}), 400

@api.route('/delete/<string:id>', methods=['DELETE'])
def removeAnimal(id):
    animal = Animal.query.get(id)
    if not animal:
        return jsonify({'Removal failed': f"No animal with ID {id} was found in the database."}), 400
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'Removed animal': animal.to_dict()}), 200