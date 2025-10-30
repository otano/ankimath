import csv
import genanki
import argparse
import random

# ID du modèle de carte, généré aléatoirement pour être unique.
# Il est important que cela reste constant pour un type de carte donné.
MODEL_ID = 1607392319

# Style CSS pour les cartes.
CSS = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
.latex {
 font-size: 1.5em;
}

.mjx-mi { color: red; }     /* variables */
.mjx-mn { color: green; }   /* nombres */
.mjx-mo { color: blue; }    /* opérateurs */
"""
±
def create_anki_deck(input_file, output_file):
    """
    Crée un paquet Anki (.apkg) à partir d'un fichier CSV.
    """
    # Définition du modèle de carte Anki (template)
    # Ce modèle inclut le support pour MathJax en entourant les champs de `\(...\)`
    anki_model = genanki.Model(
        MODEL_ID,
        'math_formulae',
        fields=[
            {'name': 'Recto'},
            {'name': 'VersoSolution'},
            {'name': 'VersoInfos'},
        ],
        templates=[
            {
                'name': 'math',
                'qfmt': r'<div class="latex">\({{Recto}}\)</div>',
                'afmt': r'{{FrontSide}}<hr id="answer"><div class="latex">\({{VersoSolution}}\)</div><br><small>{{VersoInfos}}</small>',
            },
        ],
        css=CSS)

    # Création du paquet Anki
    anki_deck = genanki.Deck(
        # 1 << 30 en d'autre terme 1 * 2**30, c.a.d  1,073,741,824.
        # technique pour se faire un unique id en tapant alléatoirement dans une fourchette massive 
        random.randrange(1 << 30, 1 << 31),
        'Trigonométrie via CSV'
    )

    # Lecture du fichier CSV et ajout des notes
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                note = genanki.Note(
                    model=anki_model,
                    fields=[row['recto'], row['verso_solution'], row['verso_infos']]
                )
                anki_deck.add_note(note)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{input_file}' n'a pas été trouvé.")
        return
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du CSV : {e}")
        return

    # Génération du fichier .apkg
    genanki.Package(anki_deck).write_to_file(output_file)
    print(f"Le paquet Anki '{output_file}' a été créé avec succès !")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crée un paquet Anki (.apkg) à partir d'un fichier CSV pour des révisions de math.")
    parser.add_argument('--input', dest='input_file', default='formulas.csv',
                        help="Chemin vers le fichier CSV d'entrée (par défaut: formulas.csv)")
    parser.add_argument('--output', dest='output_file', default='trigo_deck.apkg',
                        help="Chemin vers le fichier .apkg de sortie (par défaut: trigo_deck.apkg)")

    args = parser.parse_args()
    create_anki_deck(args.input_file, args.output_file)