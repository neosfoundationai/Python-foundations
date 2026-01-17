from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


load_dotenv()
client = OpenAI()


def get_input() -> str:
    logger.info("Acquisition de l'entrée utilisateur")

    while True:
        texte = input("Quel est ton texte à résumer ? : ").strip()

        if not texte:
            logger.warning("Texte vide fourni par l'utilisateur")
            print("⚠️ Le texte ne peut pas être vide")
            continue

        logger.info("Texte utilisateur valide (%d caractères)", len(texte))
        return texte


def process_with_ia(texte: str) -> str:
    logger.info("Appel au service IA")

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            max_output_tokens=200,
            input=[
                {
                    "role": "system",
                    "content": "Tu es un expert en synthèse de texte claire et structurée."
                },
                {
                    "role": "user",
                    "content": f"Résume le texte suivant en 5 points clairs :\n\n{texte}"
                }
            ]
        )

        logger.info("Réponse IA reçue avec succès")
        return response.output_text

    except OpenAIError as e:
        logger.error("Erreur OpenAI : %s", e)
        raise RuntimeError("Service IA indisponible")

    except TimeoutError:
        logger.error("Timeout lors de l'appel OpenAI")
        raise RuntimeError("Service IA trop lent")


def post_process(resultat: str) -> None:
    logger.info("Post-traitement du résultat")

    resultat = resultat.strip()

    print("\n--- RÉSULTAT ---\n")
    print(resultat)

    logger.info("Affichage du résultat terminé")


def main():
    logger.info("Démarrage du pipeline IA")

    try:
        texte = get_input()
        resultat = process_with_ia(texte)
        post_process(resultat)

    except RuntimeError as e:
        logger.warning("Erreur contrôlée : %s", e)
        print("❌", e)

    except Exception as e:
        logger.critical("Crash inattendu", exc_info=True)
        print("💥 Crash inattendu :", e)

    finally:
        logger.info("Fin du script")


if __name__ == "__main__":
    main()
    