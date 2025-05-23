# verification.py (cog)

import random
from discord.ext import commands

user_codes = {}

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        if ctx.guild is not None:
            await ctx.send("Please use this command in DMs only.")
            return

        code = ''.join(str(random.randint(0, 9)) for _ in range(6))
        user_codes[code] = ctx.author.id
        await ctx.send(f"Your verification code: `{code}`")

    def check_code(self, code):
        return user_codes.pop(code, None)  # Remove code on use

async def setup(bot):
    cog = Verification(bot)
    await bot.add_cog(cog)
    bot.verification_cog = cog  # expose cog on bot
