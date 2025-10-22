from discord.ext import commands
import discord

emoji_to_role = {}
ROLE_MESSAGE_ID = None


class RolePollManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ===============================
    # 🔹 COMMANDS
    # ===============================

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def create_poll(self, ctx):
        """Create a new reaction-role poll."""
        embed = discord.Embed(
            title="🎯 Choose a role that you want to posses",
            description="To add options (roles) to the poll, just use `!add_poll_role <emoji> <role>` to add some!",
            color=0x00ff00
        )
        message = await ctx.channel.send(embed=embed)

        global ROLE_MESSAGE_ID
        ROLE_MESSAGE_ID = message.id

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def add_poll_role(self, ctx, emoji: str, *, role_name: str):
        """Add a new emoji → role mapping to the poll."""
        global ROLE_MESSAGE_ID
        if ROLE_MESSAGE_ID is None:
            await ctx.send("❌ No poll exists yet. Use `!create_poll` first.")
            return

        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            await ctx.send(f"❌ Role '{role_name}' not found.")
            return

        emoji_to_role[emoji] = role_name
        message = await ctx.channel.fetch_message(ROLE_MESSAGE_ID)

        desc = "React to get or remove a role:\n\n"
        for e, r in emoji_to_role.items():
            desc += f"{e} → {r}\n"

        embed = discord.Embed(
            title="🎯 Reaction Roles Poll",
            description=desc,
            color=0x00ff00
        )
        await message.edit(embed=embed)
        await message.add_reaction(emoji)
        await ctx.send(f"✅ Added mapping: {emoji} → {role_name}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def remove_poll_role(self, ctx, emoji: str):
        """Remove an emoji → role mapping from the poll."""
        global ROLE_MESSAGE_ID
        if emoji not in emoji_to_role:
            await ctx.send("❌ That emoji is not in the poll.")
            return

        del emoji_to_role[emoji]
        message = await ctx.channel.fetch_message(ROLE_MESSAGE_ID)

        if emoji_to_role:
            desc = "React to get or remove a role:\n\n" + "\n".join(
                f"{e} → {r}" for e, r in emoji_to_role.items()
            )
        else:
            desc = "No roles currently set."

        embed = discord.Embed(
            title="🎯 Reaction Roles Poll",
            description=desc,
            color=0x00ff00
        )
        await message.edit(embed=embed)
        await ctx.send(f"🗑️ Removed mapping for {emoji}")

    # ===============================
    # 🔹 REACTION HANDLERS
    # ===============================

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Assign role when a user reacts."""
        if (
                payload.user_id == self.bot.user.id
                or ROLE_MESSAGE_ID is None
                or payload.message_id != ROLE_MESSAGE_ID
        ):
            return

        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        emoji = payload.emoji.name

        if emoji not in emoji_to_role:
            channel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            await message.remove_reaction(payload.emoji, member)
            return

        role = discord.utils.get(guild.roles, name=emoji_to_role[emoji])
        if role:
            await member.add_roles(role)
            print(f"✅ Added role '{role.name}' to {member.name}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Remove role when a user removes their reaction."""
        if ROLE_MESSAGE_ID is None or payload.message_id != ROLE_MESSAGE_ID:
            return

        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role_name = emoji_to_role.get(payload.emoji.name)
        if not role_name:
            return

        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await member.remove_roles(role)
            print(f"❌ Removed role '{role.name}' from {member.name}")


async def setup(bot):
    await bot.add_cog(RolePollManagement(bot))
