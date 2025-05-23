import aiohttp
from discord.ext import commands

class TotalClan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def totalclan(self, ctx):
        url = "https://ps99.biggamesapi.io/api/clansList"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    await ctx.send("❌ Failed to fetch clan list. Please try again later.")
                    return
                data = await response.json()

        if data.get("status") != "ok":
            await ctx.send("❌ Failed to retrieve valid data.")
            return

        total_clans = len(data.get("data", []))
        await ctx.send(f"🏰 There are currently **{total_clans}** clans in total.")

async def setup(bot):
    await bot.add_cog(TotalClan(bot))
