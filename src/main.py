# src/main.py

import sys
import json
import os
from datetime import datetime
from src.transcription import transcrire_audio
from src.summary import generer_compte_rendu


def sauvegarder_compte_rendu(compte_rendu: dict, chemin_audio: str) -> str:
    """
    Sauvegarde le compte rendu dans un fichier Markdown daté.
    """
    # Créer le dossier outputs s'il n'existe pas
    os.makedirs("outputs", exist_ok=True)

    # Nom du fichier avec la date
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"outputs/compte_rendu_{date}.md"

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"# {compte_rendu.get('titre', 'Compte rendu')}\n\n")
        f.write(f"## Résumé\n{compte_rendu.get('resume', '')}\n\n")

        f.write("## Points clés\n")
        for point in compte_rendu.get('points_cles', []):
            f.write(f"- {point}\n")

        f.write("\n## Décisions\n")
        decisions = compte_rendu.get('decisions', [])
        if decisions:
            for d in decisions:
                f.write(f"- {d}\n")
        else:
            f.write("Aucune décision.\n")

        f.write("\n## Actions\n")
        actions = compte_rendu.get('actions', [])
        if actions:
            for a in actions:
                f.write(f"- {a}\n")
        else:
            f.write("Aucune action.\n")

    return nom_fichier


def main():
    # Vérifier qu'un fichier audio est fourni
    if len(sys.argv) < 2:
        print(" Usage : python src/main.py <chemin_audio>")
        sys.exit(1)

    chemin_audio = sys.argv[1]

    # 1) Transcription
    print("\n Étape 1 : Transcription en cours...")
    texte = transcrire_audio(chemin_audio)
    print(f" Transcription terminée ({len(texte)} caractères)")

    # 2) Génération du compte rendu
    print("\n Étape 2 : Génération du compte rendu...")
    compte_rendu = generer_compte_rendu(texte)
    print(" Compte rendu généré !")

    # 3) Affichage
    print("\n=== COMPTE RENDU ===")
    print(json.dumps(compte_rendu, indent=2, ensure_ascii=False))

    # 4) Sauvegarde
    fichier = sauvegarder_compte_rendu(compte_rendu, chemin_audio)
    print(f"\n Compte rendu sauvegardé : {fichier}")


if __name__ == "__main__":
    main()