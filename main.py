import discord
import logging
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Logging setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix='!', intents=intents)


# Load cogs
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")


async def load_extensions():
    await bot.load_extension("cogs.member_management")
    await bot.load_extension("cogs.role_poll_management")


# Run
async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)


import asyncio

asyncio.run(main())
