---
name: document-audit
description: Vérifie l'inventaire documentaire, les pièces citées, les sources et les échéances juridiques d'un dossier Mibba. À utiliser pour déterminer les pièces présentes ou manquantes, retrouver les annexes d'un acte ou identifier les échéances à surveiller.
---

# Vérification documentaire Mibba

Vérifie uniquement le dossier choisi par l'utilisateur ou celui que tu identifies sans ambiguïté.

## Inventaire et pièces citées

1. Identifie le dossier avec `search_legal_records`, puis consulte-le avec `get_legal_record`.
2. Liste les documents pertinents avec `search_documents`. Utilise la pagination et les totaux disponibles. Une première page tronquée ne constitue pas un inventaire complet.
3. Si un acte cite des annexes ou des pièces promises, utilise `match_cited_documents`. Conserve les catégories `present`, `uncertain` et `absent`.
4. Pour une correspondance `uncertain`, examine la page suggérée ou recherche dans le texte avant de conclure. Un document numérisé mal nommé peut contenir la pièce citée.
5. Présente une pièce absente comme une lacune observée dans l'inventaire, et non comme la preuve que l'étude ne l'a jamais reçue.

## Échéances

Utilise `compute_dossier_deadlines` pour les délais de rétractation, l'acceptation d'une offre de prêt et l'expiration des diagnostics. Fournis uniquement les dates établies par les sources Mibba et cite les pages correspondantes. Utilise cet outil pour les calculs juridiques qu'il prend en charge.

## Résultat

Regroupe les résultats en pièces présentes, correspondances incertaines, lacunes observées et échéances. Place les citations Mibba à côté de chaque constat important et précise les limites dues aux documents illisibles ou non synchronisés.
