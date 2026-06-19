import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.system_channel:
            embed = discord.Embed(
                title="🎉 Welcome!",
                description=f"Welcome {member.mention} to **{member.guild.name}**!",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await member.guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.system_channel:
            embed = discord.Embed(
                title="👋 Goodbye!",
                description=f"**{member}** left the server.",
                color=discord.Color.red()
            )
            await member.guild.system_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
