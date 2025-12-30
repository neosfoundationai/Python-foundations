import requests

def get_age_prediction(name):
    url = "https://api.agify.io"

    try:
        response = requests.get(url, params={"name": name}, timeout=5)
        response.raise_for_status()  # déclenche HTTPError si != 200
        data = response.json()

        if "age" not in data or "count" not in data:
            raise KeyError("Clé manquante dans la réponse API")

        return data

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erreur API : {e}")


def display_result(data):
    print("\n--- RESULT ---")
    print(f"Name : {data['name']}")
    print(f"Predicted age : {data['age']}")
    print(f"Sample size : {data['count']}")


def main():
    while True:
        try:
            name = input("What is your name? : ").strip()

            if not name:
                raise ValueError("Nom vide")

            if not name.isalpha():
                raise ValueError("Nom invalide")

            result = get_age_prediction(name)
            display_result(result)
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
