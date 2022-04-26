from flask import Blueprint, jsonify


class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


planets = [Planet(1, "Mercury", "blue"),
           Planet(2, "Venus", "round"),
           Planet(3, "PizzaPlanet", "pepperoni")]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planet_reply = []
    for planet in planets:
        planet_reply.append({"id": planet.id,
                             "name": planet.name,
                             "description": planet.description})

    return jsonify(planet_reply)

@planet_bp.route("<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"msg": f"Planet ID must be numerical: {planet_id}"}, 400
    
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
    return {"msg": f"Planet ID not found: {planet_id}"}, 404
