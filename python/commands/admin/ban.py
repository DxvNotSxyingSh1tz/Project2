import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Owner")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 Banned {member.mention} | Reason: {reason or 'No reason provided'}")

async def setup(bot):
    await bot.add_cog(Ban(bot))
