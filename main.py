# Built in Python 3.13
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import yaml

# load from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# load from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
COGS = config.get("cogs",[])
LOG_CHANNEL = config["bot"]["log-channel"]

# set discord intents
intents = discord.Intents.default()
intents.message_content = True  # REQUIRED for prefix commands

bot = commands.Bot(command_prefix='!', intents=intents)

# Attach utils
# ---

async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(f"cogs.{cog}")
            print(f"Loaded {cog}")
        except Exception as e:
            print(f"Failed to load {cog}: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Log Channel: {LOG_CHANNEL}")
    loginMessage = f"```cataphracts-helper online\nlogged in as: {bot.user.name}\nbot user id: {bot.user.id}```"
    await bot.get_channel(LOG_CHANNEL).send(loginMessage)
    print("Ready!")

@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())