question1 = input("Es-tu B2B ou B2C ? :")
question2 = input("As-tu deja des clients payants ? oui/non :")
question3 = input("Ton objectif principal est-il: vitesse, revenu, apprentissage ? :")
question4 = input("A tu une audiance existante ? oui/non :")
question5 = input("As-tu un budget ? oui/non :")

profil_detecte = question1, question2, question3

print( "analyse termine .")
print("==== PROFIL ===")
print(f"Ton profil est {question1}, clients payants = {question2},{question3},  audiance existante = {question4}, budget = {question5}")

if question1 == "B2B" and question2 == "non":
    print ("Valide ton offre avec quelques entreprises pilotes avant de scaler.")

elif question1 == "B2B" and question2 == "oui":
    print("structure ton process de vente et automatise progressivement.")

elif question1 == "B2B" and question5 == "oui":
    print("Ne code pas tout de suite, concentre-toi sur la distribution et le marketing.")

elif question3 == "apprentissage":
    print("Faix un scrpit simple ou un MVP technique pour apprendre.")

elif question3 == "revenue":  
    print("Creer une offre simple et monetisable rapidement")

elif question3 == "vitesse":
    print("utiliser des outils no-code pour aller vite.")

elif question4 == "oui" and question5 == "oui":
    print("Commence a vendre !")
 
elif question5 == "non":
    print("Tu ne peux pas avanacer sans budget. Obtien de l'argent avant de te lancer !")

else:
    print("Profil non reconnu, precise mieux tes reponses.")

