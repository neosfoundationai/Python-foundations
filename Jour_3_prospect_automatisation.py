prospects = [
    {"name": "Alice", "type": "B2B", "status": "cold"},
    {"name": "Mehdi", "type": "B2C", "status": "warm"},
    {"name": "Sarah", "type": "B2B", "status": "hot"},
]

for personne in prospects:
    print("=== Resulat ===")
    if personne["type"] == "B2B" and personne["status"] == "hot":
        print("prospect:", personne["name"])
        print("type:", personne["type"])
        print("Action recommandé: proposer appel.")
    
    if personne["type"] == "B2B" and personne["status"] == "cold":
        print("prospect:", personne["name"])
        print("type:", personne["type"])
        print("Action recommandé: nurturig.")

    if personne["type"] == "B2C":
        print("prospect:", personne["name"])
        print("type:", personne["type"])
        print("Action recommendé: ne pas vendre directement.")