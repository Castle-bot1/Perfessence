from database import Database

class Recommender:

    def __init__(self):

        self.db = Database()

    def get_top_rated_perfumes(self, limit=5):

        query = """
        MATCH (u:Usuario)-[r:RATED]->(p:Perfume)

        RETURN
            p.nombre AS perfume,
            AVG(r.rating) AS promedio,
            COUNT(r) AS total_reviews

        ORDER BY promedio DESC, total_reviews DESC
        LIMIT $limit
        """

        result = self.db.execute_query(query, {
            "limit": limit
        })

        return result

    def recommend_for_user(self, username, limit=5):

        query = """

        MATCH (u:Usuario {nombre: $username})-[:RATED]->(p:Perfume)

        MATCH (other:Usuario)-[:RATED]->(p)

        MATCH (other)-[r:RATED]->(recommended:Perfume)

        WHERE other <> u

        RETURN
            recommended.nombre AS perfume,
            recommended.marca AS marca,
            recommended.intensidad AS intensidad,
            recommended.precio AS precio,
            recommended.imagen AS imagen,
            AVG(r.rating) AS score,
            COUNT(*) AS recomendaciones

        ORDER BY score DESC, recomendaciones DESC

        LIMIT $limit
        """

        result = self.db.execute_query(query, {
            "username": username,
            "limit": limit
        })

        return result

    def recommend_from_quiz(self, username, limit=5):

        query = """
        MATCH (u:Usuario {nombre: $username})

        MATCH (p:Perfume)-[:PERTENECE_A]->(f:Familia)
        MATCH (p)-[:IDEAL_PARA]->(o:Ocasion)

        WITH p, u,

            CASE
                WHEN f.nombre = u.familia_favorita THEN 5
                ELSE 0
            END

            +

            CASE
                WHEN o.nombre = u.ocasion THEN 3
                ELSE 0
            END

            +

            CASE
                WHEN u.intensidad = 'Baja'
                    AND p.intensidad = 'EAU DE TOILETTE'
                THEN 2

                WHEN u.intensidad = 'Media'
                    AND p.intensidad = 'EAU DE PARFUM'
                THEN 2

                WHEN u.intensidad = 'Alta'
                    AND (
                        p.intensidad = 'PARFUM'
                        OR p.intensidad CONTAINS 'INTENSE'
                        OR p.intensidad = 'ELIXIR'
                    )
                THEN 2

                ELSE 0
            END

            +

            CASE
                WHEN p.genero = u.tipo_usuario THEN 2
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
            p.imagen AS imagen,
            score

        ORDER BY score DESC, p.precio DESC

        LIMIT $limit
        """

        return self.db.execute_query(query, {
            "username": username,
            "limit": limit
        })

    def close(self):
        self.db.close()