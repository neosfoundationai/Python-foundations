from openai import OpenAI
from dotenv import load_dotenv


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
    text = input("Quel texte veux-tu résumer ? : ").strip()

    if not text:
        print("❌ Le texte ne peut pas être vide")
        return

    summary = summarize_text(text)

    print("\n--- SUMMARY ---")
    print(summary)


if __name__ == "__main__":
    main()    