import discord
from discord.ext import commands
from settings import firstPart, secondPart
import asyncio
import threading
from api_bridge import run_flask

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

async def load_extensions():
    await bot.load_extension("commands.clan")
    await bot.load_extension("commands.totalclan")
    await bot.load_extension("commands.admin.kick")
    await bot.load_extension("commands.admin.purge")
    await bot.load_extension("commands.admin.ban")
    await bot.load_extension("commands.dadjoke")
    await bot.load_extension("commands.verification")

async def start_bot():
    await load_extensions()
    await bot.start(firstPart + secondPart)

def run_bot():
    asyncio.run(start_bot())

if __name__ == "__main__":
    # Run Flask API with access to the bot
    flask_thread = threading.Thread(target=run_flask, args=(bot,))
    flask_thread.start()

    # Start the Discord bot
    run_bot()
