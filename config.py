import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

PREFIX = "!"

EMBED_COLOR = 0x5865F2

BOT_NAME = "QueenZzz"
BOT_VERSION = "1.0.0"
