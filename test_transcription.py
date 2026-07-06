# test_transcription.py

from src.transcription import transcrire_audio

texte = transcrire_audio("audio/AUDIO-2026-06-30-11-25-08.m4a")
print("\n=== TRANSCRIPTION ===")
print(texte)