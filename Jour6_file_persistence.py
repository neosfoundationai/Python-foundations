def save_user_to_file(user, filename="users.txt", separator="|"):
    """
    Sauvegarde un dictionnaire utilisateur dans un fichier texte.
    """
    with open(filename, "a", encoding="utf-8") as f:
        for key, value in user.items():
            f.write(f"{key}{separator}{value}\n")
        f.write("---\n")  # séparateur entre utilisateurs


def load_users_from_file(filename="users.txt", separator="|"):
    """
    Charge tous les utilisateurs depuis le fichier
    et retourne une liste de dictionnaires.
    """
    users = []
    current_user = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line == "---":
                users.append(current_user)
                current_user = {}
                continue

            key, value = line.split(separator, 1)
            current_user[key] = value

    return users


def display_user_summary(users):
    """
    Affiche un résumé structuré des utilisateurs.
    """
    print("\n=== RÉSUMÉ UTILISATEURS ===\n")

    for index, user in enumerate(users, start=1):
        print(f"Utilisateur {index}")
        for key, value in user.items():
            print(f"- {key} : {value}")
        print("-" * 30)


# =========================
# PROGRAMME PRINCIPAL
# =========================
if __name__ == "__main__":

    user = {
        "name": "Alice",
        "role": "Founder",
        "business_type": "B2B",
        "stage": "idea"
    }

    save_user_to_file(user)
    users_loaded = load_users_from_file()
    display_user_summary(users_loaded)
    