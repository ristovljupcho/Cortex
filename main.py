import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required to detect member joins

bot = commands.Bot(command_prefix='!', intents=intents)

predefinedRole = "Test Role"

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

# Replace this with your actual channel ID
WELCOME_CHANNEL_ID = 802286651178352650
LEAVE_CHANNEL_ID = 802286704915382323

@bot.event
async def on_member_join(member: discord.Member):
    server_name = member.guild.name
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
    else:
        print(f"Channel with ID {WELCOME_CHANNEL_ID} not found")

    # Send DM
    try:
        await member.send(f"Hello {member.name}, welcome to {server_name}! 🎉")
    except discord.Forbidden:
        print(f"Couldn't send DM to {member.name}")

    # Assign role
    role = discord.utils.get(member.guild.roles, name=predefinedRole)
    if role:
        await member.add_roles(role)
        print(f"Assigned role '{role.name}' to {member.name}")
    else:
        print(f"Role '{predefinedRole}' not found in guild '{server_name}'")

@bot.event
async def on_member_remove(member: discord.Member):
    channel = member.guild.get_channel(LEAVE_CHANNEL_ID)
    if channel:
        await channel.send(f"{member.name} has left the server. 🥲")
    else:
        print(f"Leave channel not found")

@bot.command()
async def add_role(ctx):
    role = discord.utils.get(ctx.guild.roles, name=predefinedRole)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been assigned to {role}")
    else:
        await ctx.send(f"Role doesn't exist")

@bot.command()
async def remove_role(ctx):
    role = discord.utils.get(ctx.guild.roles, name=predefinedRole)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has been unassigned from {role}")
    else:
        await ctx.send(f"Role doesn't exist")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
