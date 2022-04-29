from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


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


# @planet_bp.route("", methods=["GET"])
# def get_all_planets():
#     planet_reply = []
#     for planet in planets:
#         planet_reply.append({"id": planet.id,
#                              "name": planet.name,
#                              "description": planet.description})

#     return jsonify(planet_reply)


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
