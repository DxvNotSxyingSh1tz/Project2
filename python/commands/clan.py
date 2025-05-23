import discord
import aiohttp
from discord.ext import commands

def format_number(n):
    if n >= 1_000_000_000_000_000:
        return f"{n / 1_000_000_000_000_000:.1f}Qd"
    elif n >= 1_000_000_000_000:
        return f"{n / 1_000_000_000_000:.1f}T"
    elif n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    else:
        return str(n)

async def get_roblox_username(user_id):
    url = f"https://users.roblox.com/v1/users/{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("name")
            return None

class Clan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clan(self, ctx, clanname):
        clan_url = f"https://ps99.biggamesapi.io/api/clan/{clanname}"
        battle_url = "https://ps99.biggamesapi.io/api/activeClanBattle"

        async with aiohttp.ClientSession() as session:
            async with session.get(clan_url) as response:
                if response.status != 200:
                    await ctx.send("❌ Failed to fetch clan data.")
                    return
                clan_data = await response.json()

            if clan_data.get("status") != "ok":
                await ctx.send(f"❌ Clan `{clanname}` not found.")
                return

            clan = clan_data["data"]

            async with session.get(battle_url) as response:
                if response.status != 200:
                    await ctx.send("❌ Failed to fetch battle data.")
                    return
                battle_data = await response.json()

        total_points = 0
        contributions = battle_data.get("data", {}).get("configData", {}).get("Contributions", {})
        if contributions and clanname in contributions:
            total_points = contributions[clanname]

        members = clan.get("Members", [])
        total_diamonds = clan.get("DiamondContributions", {}).get("AllTime", {}).get("Sum", 0)
        formatted_diamonds = format_number(total_diamonds)
        owner_user_id = str(clan.get("Owner"))
        owner_username = await get_roblox_username(owner_user_id) or owner_user_id

        embed = discord.Embed(
            title=f"🏰 Clan: {clan.get('Name')}",
            description=clan.get("Desc", "No description."),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(
            url=f"https://www.roblox.com/asset-thumbnail/image?assetId={clan['Icon'].split('rbxassetid://')[-1]}&width=420&height=420&format=png"
        )
        embed.add_field(name="🆔 Owner Username", value=owner_username, inline=True)
        embed.add_field(name="🧑‍🤝‍🧑 Members", value=f"{len(members)}/{clan.get('MemberCapacity')}", inline=True)
        embed.add_field(name="📈 Guild Level", value=str(clan.get("GuildLevel")), inline=True)
        embed.add_field(name="🎖️ Officer Capacity", value=str(clan.get("OfficerCapacity")), inline=True)
        embed.add_field(name="💎 Total Diamonds", value=formatted_diamonds, inline=False)
        embed.add_field(name="⚔️ Battle Points", value=format_number(total_points), inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Clan(bot))
