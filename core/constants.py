import os
import base64
from decouple import config

OPENAI_API_KEY = base64.b64decode(config("OPENAI_API_KEY")).decode('utf-8')
GIT_TOKEN = base64.b64decode(config("GIT_TOKEN")).decode('utf-8')
LANGCHAIN_API_KEY = base64.b64decode(config("LANGCHAIN_API_KEY")).decode('utf-8')
REPO = config("REPO")
