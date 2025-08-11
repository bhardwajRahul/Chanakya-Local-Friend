# config.py configurations for Chanakya

import os
from dotenv import load_dotenv
load_dotenv()

# General App Config
APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY', str(os.urandom(24))) # Use env var or generate
DEBUG_MODE = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')

# Ollama Configuration
OLLAMA_ENDPOINT = os.environ.get('OLLAMA_ENDPOINT')
OLLAMA_MODEL_NAME = os.environ.get('OLLAMA_MODEL_NAME') # hf.co/NikolayKozloff/Jan-nano-Q8_0-GGUF:latest qwen3:30b
OLLAMA_NUM_CTX = int(os.environ.get('OLLAMA_NUM_CTX', 2048))
OLLAMA_ENDPOINT_SMALL = os.environ.get('OLLAMA_ENDPOINT_SMALL')
OLLAMA_MODEL_NAME_SMALL = os.environ.get('OLLAMA_MODEL_NAME_SMALL') # Example change
OLLAMA_NUM_CTX_SMALL = int(os.environ.get('OLLAMA_NUM_CTX_SMALL', 2048))

# stt and tts Configuration
STT_SERVER_URL = os.environ.get('STT_SERVER_URL') # Default STT API URL
TTS_ENGINE = os.environ.get('TTS_ENGINE', "coqui") # coqui (human like, fast) or chatterbox (great voice cloning, slow) or piper (fastest, but fails on some tests)
if TTS_ENGINE == "chatterbox":
    TTS_SERVER_URL = None  # Chatterbox does not use a server URL
elif TTS_ENGINE == "coqui":
    TTS_SERVER_URL = os.environ.get('TTS_SERVER_URL') 
elif TTS_ENGINE == "piper":
    TTS_SERVER_URL = os.environ.get('TTS_SERVER_URL') 

# Database Configuration
DATABASE_PATH = os.environ.get('DATABASE_PATH')

# Client Activity Tracking
CLIENT_INACTIVE_THRESHOLD = int(os.environ.get('CLIENT_INACTIVE_THRESHOLD', 10))
CLIENT_SAVE_INTERVAL = int(os.environ.get('CLIENT_SAVE_INTERVAL', 10))
CLIENT_COUNT_FILE = os.environ.get('CLIENT_COUNT_FILE', "client_count.txt")

# Paths
# Assuming chanakya.py is in the project root. If not, adjust '..' accordingly.
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)) 
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")