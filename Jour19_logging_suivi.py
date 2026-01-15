from openai import OpenAI
from dotenv import load_dotenv
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


load_dotenv()

client = OpenAI()  # la clé est lue automatiquement depuis OPENAI_API_KEY

def summarize_text(text: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Tu es un expert en synthèse de texte claire et structurée."
            },
            {
                "role": "user",
                "content": f"Résume le texte suivant en 5 points clairs :\n\n{text}"
            }
        ],
        max_output_tokens=200
    )

    return response.output_text


def main():
    logging.info("Démarrage de l’outil de résumé")
    text = input("Quel texte veux-tu résumer ? : ").strip()
    logging.info("Texte reçu (%d caractères)", len(text))
    if not text:
        logging.error("❌ Le texte ne peut pas être vide")
        return

    try:
        summary = summarize_text(text)
        logging.info("Appel au modèle LLM")
    except:
        logging.error("Erreur lors de l'appel LLM", exc_info=True)
     

    print("\n--- SUMMARY ---")
    print(summary)
    logging.info("Résumé généré avec succès")


if __name__ == "__main__":
    main()   