import discord
from discord.ext import commands
from settings import firstPart, secondPart
import threading
from api_bridge import run_flask
import asyncio  # move import to top

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

async def load_extensions():
    extensions = [
        "commands.clan",
        "commands.totalclan",
        "commands.admin.kick",
        "commands.admin.purge",
        "commands.admin.ban",
        "commands.dadjoke",
        "commands.verification",
    ]
    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f"Loaded extension: {ext}")
        except Exception as e:
            print(f"Failed to load extension {ext}: {e}")

def start_bot():
    async def setup_and_run():
        await load_extensions()
        await bot.start(firstPart + secondPart)

    asyncio.run(setup_and_run())

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, args=(bot,), daemon=True)
    flask_thread.start()
    start_bot()
