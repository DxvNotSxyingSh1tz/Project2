import discord
from discord.ext import commands
import threading
import asyncio
from api_bridge import run_flask, app

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

async def load_extensions():
    # load your extensions here
    await bot.load_extension("commands.verification")
    # load other extensions...

async def start_bot():
    await load_extensions()
    await bot.start("YOUR_BOT_TOKEN_HERE")

def flask_thread():
    run_flask()

if __name__ == "__main__":
    # Set the global bot in api_bridge so Flask can access it
    import api_bridge
    api_bridge.bot = bot

    # Run Flask server in a background thread (Waitress handles concurrency well)
    thread = threading.Thread(target=flask_thread, daemon=True)
    thread.start()

    # Run Discord bot in main thread event loop
    asyncio.run(start_bot())
