from application import app
from flask import *
from application.models import *

def format_character(character):
    return {
        "id": character.id,
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route("/")
def hello_world():
    return "<p>Hello World ! </p>"

@app.route("/characters", methods=['POST'])
def create_character():
    # retrieve the body - req.body
    data = request.json

    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])

    db.session.add(character)
    db.session.commit()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters")
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}    

@app.route("/characters/<id>")
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
        character = FriendsCharacter.query.filter_by(id=id).first()
        db.session.delete(character)
        db.session.commit()
        return "Character Deleted"


@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
        character = FriendsCharacter.query.filter_by(id=id)
        data = request.json
        character.update(dict(name=data['name'], age=data['age'], catch_phrase=data["catch_phrase"]))
        db.session.commit()
        updatedCharacter = character.first()
        return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)