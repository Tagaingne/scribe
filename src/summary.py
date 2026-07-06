# src/summary.py

import json
from groq import Groq
from src.config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)


def lire_prompt_systeme() -> str:
    """Lit le prompt système depuis le fichier texte."""
    with open("src/prompt_system.txt", "r", encoding="utf-8") as f:
        return f.read()


def generer_compte_rendu(transcription: str) -> dict:
    """
    Génère un compte rendu structuré en JSON à partir d'une transcription.
    """
    print(" Génération du compte rendu en cours...")

    prompt_systeme = lire_prompt_systeme()

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": prompt_systeme},
                {"role": "user", "content": f"Voici la transcription :\n\n{transcription}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )
    except Exception as e:
        raise RuntimeError(f" Erreur API Groq : {e}")

    contenu = response.choices[0].message.content

    try:
        compte_rendu = json.loads(contenu)
    except json.JSONDecodeError:
        raise RuntimeError(f" JSON invalide reçu : {contenu}")

    print("Compte rendu généré !")
    return compte_rendu