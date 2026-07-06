# test_summary.py

from src.transcription import transcrire_audio
from src.summary import generer_compte_rendu
import json

# 1) Transcrire l'audio
texte = transcrire_audio("audio/AUDIO-2026-06-30-11-25-08.m4a")
print("\n=== TRANSCRIPTION ===")
print(texte)

# 2) Générer le compte rendu
compte_rendu = generer_compte_rendu(texte)
print("\n=== COMPTE RENDU ===")
print(json.dumps(compte_rendu, indent=2, ensure_ascii=False))