---
name: activity-report
description: Produit des bilans complets de l'activité des dossiers Mibba, par mois ou par année. À utiliser pour compter les dossiers actifs, modifiés ou actuellement clôturés sur une année ou une période délimitée.
---

# Bilan d'activité Mibba

Utilise `get_legal_record_activity_report` plutôt que de compter une page de résultats de recherche.

## Méthode

1. Détermine l'année civile demandée ou la période exacte définie par `from` et `toExclusive`. Demande une précision seulement si la période est ambiguë.
2. Demande le bilan complet. Découpe les périodes dépassant la durée maximale prise en charge par l'outil en intervalles sans chevauchement.
3. Présente le total et la ventilation mensuelle dans le fuseau Europe/Paris.
4. Inclue les métadonnées de synchronisation et de qualité des données du bilan, notamment les dossiers sans date de modification synchronisée.

## Interprétation

Le bilan compte les dossiers à partir de leur date de modification Septeo synchronisée. Un dossier dont le statut actuel est `Clôturé` appartient au sous-ensemble des dossiers clôturés, mais ce statut n'établit pas la date du changement. Présente le résultat comme un bilan des statuts actuels. Parle de dates exactes de clôture seulement si des sources distinctes les établissent.
