import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("Owner")  # ✅ Only users with the "Owner" role can use this command
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"👢 Kicked {member.mention} | Reason: {reason or 'No reason provided'}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("❌ You need the **Owner** role to use this command.")
        else:
            await ctx.send(f"⚠️ An error occurred: {str(error)}")

async def setup(bot):
    await bot.add_cog(Kick(bot))
