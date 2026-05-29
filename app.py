from flask import Flask, render_template, request, jsonify
from recommender import Recommender

app = Flask(__name__)

recommender = Recommender()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.json

    username = data.get("username")

    recommendations = recommender.recommend_for_user(username)

    if not recommendations:
        recommendations = recommender.recommend_from_quiz(username)

    return jsonify(recommendations)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/quiz-recommend", methods=["POST"])
def quiz_recommend():

    data = request.json

    username  = data.get("username")
    family    = data.get("family")
    occasion  = data.get("occasion")
    intensity = data.get("intensity")
    gender    = data.get("gender")

    recommender.db.execute_query("""
        MERGE (u:Usuario {nombre: $username})
        SET u.familia_favorita = $family,
            u.tipo_usuario     = $gender,
            u.ocasion          = $occasion,
            u.intensidad       = $intensity
    """, {"username": username, "family": family, "gender": gender, "occasion": occasion, "intensity": intensity})

    query = """
    MATCH (p:Perfume)-[:PERTENECE_A]->(f:Familia)
    MATCH (p)-[:IDEAL_PARA]->(o:Ocasion)

    WITH p,

    CASE WHEN f.nombre = $family THEN 5 ELSE 0 END +
    CASE WHEN o.nombre = $occasion THEN 3 ELSE 0 END +

    CASE
        WHEN $intensity = 'Baja'
            AND p.intensidad = 'EAU DE TOILETTE'
        THEN 2

        WHEN $intensity = 'Media'
            AND p.intensidad = 'EAU DE PARFUM'
        THEN 2

        WHEN $intensity = 'Alta'
            AND (
                p.intensidad = 'PARFUM'
                OR p.intensidad CONTAINS 'INTENSE'
                OR p.intensidad = 'ELIXIR'
            )
        THEN 2

        ELSE 0
    END +

    CASE
        WHEN p.genero = $gender THEN 2
        WHEN p.genero = 'Unisex' THEN 1
        ELSE 0
    END

    AS score

    WHERE score > 0

    RETURN
        p.nombre AS perfume,
        p.marca AS marca,
        p.intensidad AS intensidad,
        p.precio AS precio,
        p.imagen AS imagen

    ORDER BY score DESC

    LIMIT 12
    """

    recommendations = recommender.recommend_from_quiz(username, 12)

    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug=True)