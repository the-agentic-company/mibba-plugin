---
name: dossier-research
description: Recherche les dossiers notariaux Mibba et leurs documents avec des sources vérifiables. À utiliser pour retrouver, consulter, comparer ou résumer un dossier, un client, un participant, un bien, un document ou une information conservée dans Mibba.
---

# Recherche dans les dossiers Mibba

Utilise les outils MCP Mibba pour répondre à partir de l'espace autorisé de l'utilisateur.

## Méthode

1. Identifie le dossier avant de formuler des constats détaillés. Utilise `search_legal_records` si l'utilisateur fournit un titre, une référence, un type, un statut, une période ou un identifiant Septeo. Demande une précision seulement si plusieurs dossiers plausibles restent en concurrence.
2. Utilise `get_legal_record` pour consulter les participants, les biens, les répertoires, les métadonnées documentaires, les points à traiter et les décisions humaines du dossier.
3. Retrouve les documents avec `search_documents`. Privilégie les documents dont le texte est actif si la demande porte sur leur contenu.
4. Recherche dans le contenu avec `search_document_text` pour des identifiants de documents connus, ou `search_document_evidence` pour une question sémantique dans le corpus pertinent. Suis les indications `nextSteps` et les métadonnées de budget de recherche renvoyées par l'outil.
5. Lis les pages pertinentes avec `get_document_page`, `get_document_evidence` ou `multi_get_document_evidence`. Charge uniquement les pages nécessaires lorsque leurs sources suffisent.
6. Cite les URL renvoyées par Mibba. N'invente pas d'URL de citation, de numéro de page, d'identifiant de dossier ou de document.

## Fiabilité

- Distingue les faits établis par les sources des déductions. Signale clairement les incertitudes.
- Une recherche vide ou en échec ne prouve pas l'absence d'un fait ou d'un document.
- Respecte le sujet juridique de chaque fait. Un actif, une dette ou une obligation d'une société ne concerne pas automatiquement un participant à titre personnel.
- Respecte les `humanDecisions` renvoyées par l'évaluation du dossier. Recrée un point écarté, résolu ou obsolète seulement si une source datée plus récente le justifie, et explique cette source.
- Présente les identifiants internes bruts seulement si l'utilisateur en a besoin pour une tâche technique.
- Si un outil renvoie une erreur, suis son indication de nouvelle tentative. Utilise `report_semantic_friction` si les outils sont inadaptés, ambigus, régulièrement vides ou mal délimités.

Termine par une réponse concise, ses citations et les éventuelles lacunes importantes de couverture.
