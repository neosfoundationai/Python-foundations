1) prompt = Explique moi le business.
    Pourquoi ce prompt est mauvais:
      Il est trop vague.
      Il n'impose aucune structure.
      Il ne definie pas specifiquement quel buisness.
      Il ne donne pas de contexte.
      Il ne fixe pas d'objectif
      Il laisse toutes les decicions au models

    Ce qui manque:
      Un contexte.
      une structure
      une specialisation
      un objectif
      des regles

    Ce que le LLM ne peut pas deviner:
      Un LLM ne devine rien intelligemment
      il ne devine pas:
        Objectif reel
        Contexte
        Niveau de competence
        Le format attendu
        Les contraintes importantes
        La vérité factuelle dans un cas precis
        

2) Tu es un expert en stratégie business B2B SaaS.
Contexte : une startup IA veut vendre un outil d’analyse automatique d’emails pour PME.
Objectif : identifier une proposition de valeur claire.
Contraintes :
- réponse courte
- orientée ROI
- sans jargon technique
Format :
- Problème
- Solution
- Bénéfice économique


Pourquoi ce prompt fonctionne mieux
  Parce qu’il supprime toute ambiguïté et transforme une demande vague en tâche exécutable pour un LLM.
  Il fait 3 choses essentielles :
  Il fixe un rôle clair
  Il donne un contexte précis
  Il impose un cadre de sortie strict
    Un LLM performe quand il est contraint, pas quand il est libre.


Rôle de chaque section
1️⃣ Rôle
  « Tu es un expert en stratégie business B2B SaaS »
  🔹 Effet
    Active un registre de réponses spécifique
    Oriente le vocabulaire, les priorités, les exemples
  🔹 Pourquoi c’est clé
    Le LLM n’a pas d’identité → tu lui en donnes une.
    Sans rôle, il répondrait de manière générique.


2️⃣ Contexte
« une startup IA veut vendre un outil d’analyse automatique d’emails pour PME »
  🔹 Effet
    Réduit l’espace des réponses possibles
    Évite les hors-sujets (B2C, grand compte, techno pure)
  🔹 Pourquoi c’est clé
    Le modèle ne devine pas ton marché.
    Le contexte canalise la probabilité.


3️⃣ Objectif
« identifier une proposition de valeur claire »
  🔹 Effet
    Définit ce qu’est une “bonne” réponse
    Oriente vers la synthèse, pas l’analyse technique
  🔹 Pourquoi c’est clé
    Sans objectif, le LLM optimise la longueur, pas l’utilité.


4️⃣ Contraintes
« réponse courte, orientée ROI, sans jargon technique »
  🔹 Effet
    Force la clarté
    Empêche le blabla IA
    Rend la réponse business-ready
  🔹Pourquoi c’est clé
    Les contraintes augmentent la qualité, elles ne la réduisent pas.


5️⃣ Format
« Problème / Solution / Bénéfice économique »
  🔹 Effet
    Impose une structure logique
    Facilite la lecture et la réutilisation
  🔹 Pourquoi c’est clé
    Un LLM excelle dans les structures explicites.
    Le format agit comme un template de sortie.


3) Tu es un consultant IA senior.
Client : cabinet de recrutement (10 employés).
Problème : perte de temps sur tri de CV.
Objectif : proposer 3 idées d’automatisation IA simples.
Contraintes :
- pas de ML complexe
- rapide à implémenter
- bénéfice chiffrable

Qui paierait pour ça:
  Le cabinet de recrutement lui-même,
  le dirigeant du cabinet,
  le manager RH / recruteur senior


Pourquoi maintenant:
  Parce que le problème est devenu critique :
  explosion du volume de candidatures,
  candidatures de plus en plus hétérogènes,
  pression sur les délais de recrutement,
  pénurie de recruteurs expérimentés


À quel prix approximatif
  Pour un cabinet de 10 employés :
  Modèle réaliste:
    50 à 150 € / mois par recruteur
    soit 500 à 1 500 € / mois pour le cabinet
  Pourquoi ce prix est acceptable
    1 heure recruteur ≈ 40–80 €
    l’outil économise plusieurs heures par semaine
    ROI visible en moins d’un mois

👉 Le prix est inférieur au coût du problème.


4) PROMPT DANGEREUX (ANTI-PROMPT)
Explique-moi l’intelligence artificielle de manière simple mais très approfondie,
pour tout le monde et pour des experts,
avec beaucoup de détails mais sans être trop long,
en restant très technique mais sans jargon,
en donnant des exemples concrets et abstraits,
en une seule phrase mais aussi sous forme de liste,
en tenant compte du contexte actuel et futur,
et fais-le rapidement mais avec précision.

  Pourquoi ce prompt produira de la merde:
    Il est trop vague,
    Il est contradictoire,
    Il est trop long mais mal structuré,
    Il force le modèle à halluciner de la cohérence,
    Il laisse trop de liberté décisionnelle,
    Résultat attendu (prévisible)