def creer_prospects():
    prospects = []
    n = int(input("Combien de prospects ? "))

    for i in range(n):
        print(f"\nProspect {i + 1}")
        prospect = {
            "name": input("Nom : "),
            "type": input("Type (B2B / B2C) : "),
            "status": input("Statut (hot / warm / cold) : ")
        }
        prospects.append(prospect)

    return prospects






def analyze_prospect(prospect):
    """
    Analyse un prospect et retourne une recommandation
    """
    if prospect["type"] == "B2B" and prospect["status"] == "hot":
        return "Proposer un appel de vente"

    elif prospect["type"] == "B2B" and prospect["status"] == "cold":
        return "Envoyer du contenu éducatif (nurturing)"

    elif prospect["type"] == "B2C":
        return "Ne pas vendre directement"

    else:
        return "Profil non reconnu"
    


def display_recommendation(prospect, recommendation):
    """
    Affiche les informations du prospect + la recommandation
    """
    print("=== RÉSULTAT ===")
    print("Prospect :", prospect["name"])
    print("Type :", prospect["type"])
    print("Statut :", prospect["status"])
    print("Action recommandée :", recommendation)
    print("----------------")




def process_prospects(prospects):
    """
    Orchestration générale
    """
    for prospect in prospects:
        recommendation = analyze_prospect(prospect)
        display_recommendation(prospect, recommendation)


if __name__ == "__main__":
    prospects = creer_prospects()
    process_prospects(prospects)