from recommender import Recommender

recommender = Recommender()

username = "Fernanda"

recommendations = recommender.recommend_for_user(username)

print(f"\nRecomendaciones para {username}\n")

for perfume in recommendations:

    print("-------------------")
    print(f"Perfume: {perfume['perfume']}")
    print(f"Score: {perfume['score']:.2f}")
    print(f"Coincidencias: {perfume['recomendaciones']}")

recommender.close()