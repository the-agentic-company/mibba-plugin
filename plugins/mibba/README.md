# Plugin Mibba

Vos dossiers iNot et Fiducial directement dans ChatGPT, Codex ou Claude, via Mibba.

Connectez ChatGPT, Codex ou Claude Code aux dossiers notariaux et aux documents accessibles avec votre compte Mibba.

## Prérequis

- Un compte Mibba avec accès à au moins un espace de travail.
- Un client ChatGPT, Codex ou Claude Code compatible avec les plugins et les serveurs MCP distants.

## Fonctionnalités

- Retrouvez les dossiers, participants, biens et inventaires documentaires.
- Recherchez dans les documents avec des citations à la page fournies par Mibba.
- Vérifiez les pièces citées et calculez les échéances prises en charge.
- Préparez des bilans complets de l'activité des dossiers, par mois ou par année.

Lors de la première utilisation d'un outil Mibba, terminez la connexion et l'autorisation Mibba dans le navigateur.

## Compétences

- `mibba` présente Mibba et explique comment retrouver les informations iNot ou Fiducial synchronisées via le MCP Mibba. Claude Code l'expose avec `/mibba:mibba`. Le nom de la commande dépend du client.
- `dossier-research` recherche les dossiers et documents avec leurs sources.
- `document-audit` vérifie les inventaires, les pièces citées et les échéances.
- `activity-report` produit des bilans complets sur une période délimitée.

## Accès aux données et confidentialité

Ce plugin ne contient aucun code exécutable, automatisme de cycle de vie, dispositif de télémétrie ou mécanisme local de gestion des identifiants. Il se connecte uniquement à `https://mcp.mibba.co/mcp`.

L'assistant transmet à Mibba les arguments des appels d'outils autorisés. Mibba renvoie les données de l'espace autorisé lors de la connexion OAuth. Le serveur vérifie que l'utilisateur connecté appartient toujours à cet espace et limite chaque requête à ce périmètre. ChatGPT, Codex ou Claude traite les données renvoyées selon les conditions du produit utilisé.

Vous pouvez révoquer la connexion depuis Mibba ou les paramètres des connecteurs de votre assistant. La désactivation ou la désinstallation du plugin empêche le chargement de ses compétences et de sa configuration MCP.

## Assistance

Consultez [l'assistance Mibba](https://mibba.co/contact), la [politique de confidentialité](https://mibba.co/politique-de-confidentialite) et les [conditions d'utilisation](https://mibba.co/conditions-generales-utilisation).
