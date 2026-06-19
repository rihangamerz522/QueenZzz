import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Logged in as: {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print("QueenZzz is Online!")
    print("=" * 40)

initial_extensions = [
    "cogs.moderation",
    "cogs.welcome",
    "cogs.automod",
    "cogs.security",
    "cogs.logging",
    "cogs.tickets",
    "cogs.utility",
]

async def load_extensions():
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded: {extension}")
        except Exception as e:
            print(f"Failed to load {extension}: {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
