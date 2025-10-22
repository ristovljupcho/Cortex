import discord
from discord.ext import commands

WELCOME_CHANNEL_ID = 802286651178352650
LEAVE_CHANNEL_ID = 802286704915382323
PREDEFINED_ROLES = ["Member", "DJ"]


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}! 🎉")
        try:
            await member.send(f"Hello {member.name}, welcome to {member.guild.name}! 🎉")
        except discord.Forbidden:
            print(f"Couldn't send DM to {member.name}")

        # Assign predefined roles to new member
        for role in PREDEFINED_ROLES:
            server_role = discord.utils.get(member.guild.roles, name=role)
            if role:
                await member.add_roles(server_role)
                print(f"Added {server_role} to {member.name}")
            else:
                print(f"Couldn't add {role} to {member.name}")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = member.guild.get_channel(LEAVE_CHANNEL_ID)
        if channel:
            await channel.send(f"{member.name} has left the server. 🥲")


async def setup(bot):
    await bot.add_cog(Events(bot))
