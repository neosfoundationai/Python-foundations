JOUR 17 – Prompt Engineering:

1) Texte de test (input)
    L’intelligence artificielle transforme de nombreux secteurs.
    Elle permet d’automatiser des tâches, d’analyser de grandes quantités de données
    et d’améliorer la prise de décision. Cependant, elle soulève aussi des questions
    éthiques, notamment sur l’emploi, la transparence et la protection des données.


Prompt 1 — ❌ Basique (faible):
    Résume ce texte.

    Résultat attendu
      Résumé vague

      Pas de structure

      Qualité aléatoire

      ❌ Problèmes
        Pas de rôle
        Pas de contrainte
        Pas de format demandé


Prompt 2 — ⚠️ Moyen (mieux):
Résume ce texte en quelques phrases.


Résultat attendu
    Résumé plus court
    Toujours peu structuré
    ⚠️ Limites
      “quelques phrases” = flou
      Pas de public cible
      Pas de format clair



 Prompt 3 — ✅ Bon prompt (recommandé):
    Tu es un expert en synthèse de contenu.
    Résume le texte suivant en 5 points clairs et concis.
    Utilise un langage simple et professionnel.
    Texte :
      [L’intelligence artificielle transforme…]

    ✅ Améliorations
      Rôle défini
      Format imposé
      Résultat prévisible

Prompt 4 — ⭐ Prompt expert (très bon):
    Tu es un consultant senior en innovation technologique.
    Ta mission :
      - Résumer le texte ci-dessous
      - En 5 points maximum
      - Chaque point doit faire une seule phrase
      - Ton public est un dirigeant non technique
    Texte :
      [L’intelligence artificielle transforme…]

    Avantages:
      Contexte métier
      Public cible
      Contraintes strictes
      Sortie exploitable directement



2) Comparaison des prompts (tableau):
| Prompt   | Qualité      | Structure     | Exploitable     |
| -------- | -----------  | ------------  | -------------   |
| Prompt 1 | ❌ Faible    | ❌ Non        | ❌ Non         |
| Prompt 2 | ⚠️ Moyen     | ❌ Non        | ⚠️ Peu         |
| Prompt 3 | ✅ Bon       | ✅ Oui        | ✅ Oui         |
| Prompt 4 | ⭐ Excellent | ⭐ Très clair | ⭐ Directement |


3) Conclusion:
    Ce TP montre que la qualité d’un prompt influence directement la qualité des réponses d’un LLM.
    Un prompt précis, contextualisé et contraint permet d’obtenir des résultats fiables, structurés et exploitables en contexte professionnel.
