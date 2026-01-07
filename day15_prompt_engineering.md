import re

def clean_email(email):
    """Nettoie un email (espaces + minuscules)"""
    return email.strip().lower()

def is_valid_email(email):
    """Vérifie si un email est valide avec regex"""
    pattern = r"^[a-z0-9_.-]+@[a-z0-9-]+\.(fr|eu|com|en|us)$"
    return re.fullmatch(pattern, email) is not None

def process_emails(liste_emails):
    emails_valides = []
    emails_invalides = []

    for email in liste_emails:
        email_clean = clean_email(email)

        if is_valid_email(email_clean):
            emails_valides.append(email_clean)
        else:
            emails_invalides.append(email_clean)

    return emails_valides, emails_invalides

def affichage(emails_valides, emails_invalides):
    print("\n--- EMAILS VALIDES ---")
    for email in emails_valides:
        print(email)

    print("\n--- EMAILS INVALIDES ---")
    for email in emails_invalides:
        print(email)

def main():
    liste_emails = [
        "alice@example.com",
        "bob.smith@example.com",
        " JOHN_DOE@example.com ",
        "contact123@example.com",
        "user-name@example.com",
        "a.b.c@example.com",
        "user42@example.com",
        "firstname.lastname@example.com",
        "il@;com",
    ]

    emails_valides, emails_invalides = process_emails(liste_emails)
    affichage(emails_valides, emails_invalides)

if __name__ == "__main__":
    main()
