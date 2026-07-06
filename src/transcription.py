# src/transcription.py

import os
from groq import Groq
from src.config import GROQ_API_KEY, STT_MODEL

client = Groq(api_key=GROQ_API_KEY)


def transcrire_audio(chemin_audio: str) -> str:
    """
    Transcrit un fichier audio en texte via l'API Groq (Whisper).
    """
    # Vérifier que le fichier existe
    if not os.path.exists(chemin_audio):
        raise FileNotFoundError(f"❌ Fichier audio introuvable : {chemin_audio}")

    print(f"🎙️ Transcription en cours : {chemin_audio}")

    # Ouvrir et envoyer le fichier à l'API Groq
    with open(chemin_audio, "rb") as fichier_audio:
        try:
            transcription = client.audio.transcriptions.create(
                file=(os.path.basename(chemin_audio), fichier_audio),
                model=STT_MODEL,
                language="fr",
                response_format="verbose_json"
            )
        except Exception as e:
            raise RuntimeError(f"❌ Erreur API Groq : {e}")

    print("✅ Transcription terminée !")
    return transcription.text