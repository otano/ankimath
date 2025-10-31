# MATH REVISION
## sur ANKI

> [!note] l'objectif de cette app est d'envoyer par fichier .csv,des questions mathématiques avec une gestion de latex simplifié.

> [!TIP]le fichier de csv peut être "facilement gérer par un LLM avec un prompt adequat

├── formulas.csv // le fichier des questions mathématique

├── main.py     //le programme de traduction

├── pyproject.toml //fichier de config UV

├── README.md //ce que vous êtes en train de lire

├── trigo_deck.apkg //le paquet de carte a importer dans Anki desktop

└── uv.lock. //fichier de config UV

une fois votre paquet de carte importé synchoniser votre compte Anki pour voir vos nouvelles cartes dans votre smartphone.

installation :
une fois cloner aller avec votre terminal à la racine du projet et 
```bsh
uv sync
````

Si uv n'est pas installé sur votre machine 

```bsh
pip install uv
````

[si vous voulez en savoir plus sur uv](https://github.com/astral-sh/uv)

Enjoy !
