import os, sys
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY")