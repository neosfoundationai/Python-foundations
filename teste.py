def summarize_user(user):
    """
    Retourne un résumé structuré d’un utilisateur
    """
    summary = (
        f"Utilisateur : {user['name']}\n"
        f"Rôle : {user['role']}\n"
        f"Type de business : {user['business_type']}\n"
        f"Stade : {user['stage']}\n"
    )
    return summary 

def display_user_summary(user):
    for user in users:
        print("===Profil Utilisatuer===")
        print(summarize_user(user))
        print("----------------------------")


if __name__ == "__main__":
    users = [
        {
            "name": "Alice",
            "role": "Founder",
            "business_type": "B2B",
            "stage": "idea"
        },
        {
            "name": "Mehdi",
            "role": "Marketer",
            "business_type": "B2C",
            "stage": "early"
        },
        {
            "name": "Sarah",
            "role": "CEO",
            "business_type": "B2B",
            "stage": "scaling"
        }
    ]
    display_user_summary(users)