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

Male = "Male"


@bot.event
async def on_ready():
    print(f"We are ready to go, {bot.user.name}")


@bot.event
async def on_member_join(member):
    await member.send(f"How did you find this place {member.name} who do you work for?")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "fuck" in message.content.lower():
        await message.channel.send(f"Don't say fuck {message.author.mention}, shithead")

    await bot.process_commands(message)


# hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=Male)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} congratz your a {Male}")
    else:
        ctx.send("Sorry something went wrong ig")


@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=Male)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} is no longer a {Male}, Sad")
    else:
        ctx.send("Sorry something went wrong ig")


@bot.command()
@commands.has_role(Male)
async def sup(ctx):
    await ctx.send("yoo, what's up bro")


@sup.error
async def sup_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("are you a dude?")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
