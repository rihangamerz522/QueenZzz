import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a member")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):
        await member.ban(reason=reason)

        embed = discord.Embed(
            title="🔨 Member Banned",
            description=f"**{member}** has been banned.\nReason: **{reason}**",
            color=discord.Color.red()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="kick", description="Kick a member")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):
        await member.kick(reason=reason)

        embed = discord.Embed(
            title="👢 Member Kicked",
            description=f"**{member}** has been kicked.\nReason: **{reason}**",
            color=discord.Color.orange()
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
