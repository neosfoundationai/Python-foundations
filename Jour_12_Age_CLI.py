import requests
import argparse


class AgePredictionService:
    def __init__(self, name, base_url="https://api.agify.io"):
        self.name = name
        self.base_url = base_url

    def call_api(self):
        try:
            response = requests.get(
                self.base_url,
                params={"name": self.name},
                timeout=5
            )
            response.raise_for_status()
            data = response.json()

            if "age" not in data or "count" not in data:
                raise KeyError("Clé manquante dans la réponse API")

            return data

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Erreur API : {e}")

    def display(self, data, lang="en"):
        print("\n--- AGE PREDICTION ---")
        print(f"Name        : {data['name']}")
        print(f"Predicted   : {data['age']} years")
        print(f"Sample size : {data['count']}")


def main():
    parser = argparse.ArgumentParser(
        description="CLI de prédiction d'âge via API Agify"
    )

    parser.add_argument(
        "--name",
        required=True,
        type=str,
        help="Nom de la personne à analyser"
    )

    parser.add_argument(
        "--lang",
        default="en",
        type=str,
        help="Langue d'affichage (optionnel)"
    )

    args = parser.parse_args()

    try:
        if not args.name.isalpha():
            raise ValueError("Le nom doit contenir uniquement des lettres")

        service = AgePredictionService(args.name)
        data = service.call_api()
        service.display(data, args.lang)

    except ValueError as e:
        print(f"❌ Erreur utilisateur : {e}")
    except KeyError as e:
        print(f"🗝️ Erreur données API : {e}")
    except RuntimeError as e:
        print(f"🌐 Problème API : {e}")
    except Exception as e:
        print(f"💥 Erreur inattendue : {e}")

    print("\n✅ Fin du programme")


if __name__ == "__main__":
    main()