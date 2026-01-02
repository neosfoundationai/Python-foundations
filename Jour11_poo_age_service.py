import requests


class AgePredictionService:
    def __init__(self, nom, base_url="https://api.agify.io"):
        self.nom = nom
        self.base_url = base_url

    def appel_api(self):
        try:
            response = requests.get(
                self.base_url,
                params={"name": self.nom},
                timeout=5
            )
            response.raise_for_status()

            data = response.json()

            if "age" not in data or "count" not in data:
                raise KeyError("Clé manquante dans la réponse API")

            return data

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Erreur API : {e}")

    def display(self, data):
        print("\n--- RESULT ---")
        print(f"Name : {data['name']}")
        print(f"Predicted age : {data['age']}")
        print(f"Sample size : {data['count']}")


def main():
    while True:
        try:
            nom = input("Nom ? ").strip()

            if not nom:
                raise ValueError("Nom vide")

            if not nom.isalpha():
                raise ValueError("Nom invalide (lettres uniquement)")

            prediction = AgePredictionService(nom)

            data = prediction.appel_api()
            prediction.display(data)

            break

        except ValueError as e:
            print(f"❌ Erreur utilisateur : {e}")

        except KeyError as e:
            print(f"🗝️ Erreur de données : {e}")

        except RuntimeError as e:
            print(f"🌐 Problème API : {e}")

        except Exception as e:
            print(f"💥 Erreur inattendue : {e}")

    print("\n✅ Fin du programme")


if __name__ == "__main__":
    main()
 
        
    

         




        
        


