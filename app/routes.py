from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"msg": f"Planet ID must be numerical: {planet_id}"}, 400

    planet = Planet.query.get(planet_id)

    if not planet:
        return {"msg": f"Planet ID not found: {planet_id}"}, 404

    return planet


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        descr=request_body['descr'],
                        num_of_starbucks=request_body["num_of_starbucks"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created.  Good job spaceman!", 201)


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets_reply = []
    planets = Planet.query.all()
    for planet in planets:
        planets_reply.append({"name": planet.name,
                              "descr": planet.descr,
                              "num_of_starbucks": planet.num_of_starbucks,
                              "id": planet.id})
    return jsonify(planets_reply)


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "descr": planet.descr,
        "num_of_starbucks": planet.num_of_starbucks
    }


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    try:
        planet.name = request_body["name"]
        planet.descr = request_body["descr"]
        planet.num_of_starbucks = request_body["num_of_starbucks"]
    except KeyError:
        return {"msg": "Name, description and number of Starbucks required"}, 400

    db.session.commit()

    return {"msg": "Planet successfully updated",
            "id": planet.id,
            "name": planet.name,
            "descr": planet.descr,
            "num_of_starbucks": planet.num_of_starbucks
            }, 200


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def explode_one_planet(planet_id):
    planet = validate_planet(planet_id)
    print(planet.name)
    db.session.delete(planet)
    db.session.commit()

    return {"msg": f"{planet.name} exploded"}, 200

# @planet_bp.route("<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return {"msg": f"Planet ID must be numerical: {planet_id}"}, 400

#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description
#             }
#     return {"msg": f"Planet ID not found: {planet_id}"}, 404
