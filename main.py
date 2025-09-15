import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("Discord_Token")

handler = logging.FileHandler(filename="discord.log"), encoding="utf-8", mode="w"
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(commands_prefix="!!", intents=intents)