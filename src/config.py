# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Clé API Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError(" GROQ_API_KEY manquante ! Vérifie ton fichier .env")

# Modèles utilisés (définis une seule fois ici)
STT_MODEL = "whisper-large-v3"        # modèle Speech-to-Text
LLM_MODEL = "llama-3.3-70b-versatile" # modèle LLM