import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!!", intents=intents)


@bot.event
async def on_ready():
    print(f"We are ready to go, {bot.user.name}")


@bot.event
async def on_member_join(member):
    await member.send(f"How did you find this place {member.name} who do you work for?")


@bot.event
async def on_message(message):
    if message.auther == bot.user:
        return

    if "fuck" in message.content.lower():
        await message.channel.send(f"Don't say fuck {message.author.mention}, shithead")

    await bot.process_commands(message)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
