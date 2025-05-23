import discord
from discord.ext import commands
from settings import firstPart, secondPart
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

def start_bot():
    # Load extensions asynchronously before running bot
    async def setup_and_run():
        await load_extensions()
        # Use bot.start() instead of bot.run() if you want more control,
        # but bot.run() is simpler and manages event loop internally.
        # Since we want to load extensions before run, we do this:
        await bot.start(firstPart + secondPart)

    # Run the async setup and bot start in the event loop
    import asyncio
    asyncio.run(setup_and_run())

if __name__ == "__main__":
    # Run Flask in a separate thread (because app.run blocks)
    flask_thread = threading.Thread(target=run_flask, args=(bot,), daemon=True)
    flask_thread.start()

    # Start the Discord bot in main thread (blocking)
    start_bot()

