from unicodedata import name
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
