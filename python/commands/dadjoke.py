import random
import discord
from discord.ext import commands
import datetime

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dadjoke(self, ctx):
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts.",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the bot cross the road? Because someone told it to with `!move`.",
            f"{ctx.author.mention}, you're not just funny — you're *404: Sense of Humor Not Found*!",
            "*Inserts witty response here*... oh wait, I'm the bot, I have to be witty.",
            "I'm on a seafood diet. I see food and I eat it. 🤖🍣",
            "I would make a joke about construction, but I'm still working on it.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "Why did the JavaScript developer wear glasses? Because they couldn’t C#.",
            "You know you’re a bot when people expect you to be funny, helpful, and online 24/7. 😅",
            "What do you call 8 hobbits? A hob-byte. 🧙‍♂️",
            "Why don’t oysters share their pearls? Because they’re shellfish.",
            "I’m on a whiskey diet. I’ve lost three days already. 🍸",
            "I have a fear of speed bumps, but I’m slowly getting over it.",
            "I'm trying to lose weight, but it's not working. I'm on a see-food diet... I see food and I eat it.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I made a pun about the wind, but it blows.",
            "I asked the librarian if the library had any books on paranoia. She whispered, ‘They’re right behind you…’",
            "What’s orange and sounds like a parrot? A carrot.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "How do cows stay up to date with current events? They read the moo-nspapers.",
            "I used to play piano by ear, but now I use my hands.",
            "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
            "What’s the best way to watch a fly fishing tournament? Live stream.",
            "I’m writing a book on reverse psychology. Don’t buy it!",
            "I only know 25 letters of the alphabet. I don’t know y.",
            "I went to a seafood disco last week... and pulled a mussel.",
            "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
            "I’m terrified of elevators, so I’m going to start taking steps to avoid them.",
            "I couldn’t figure out how to put my seatbelt on... until it clicked.",
        ]

        meme_gifs = [
            "https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif",
            "https://media.giphy.com/media/3o7TKu8RvQuomFfUUU/giphy.gif",
            "https://media.giphy.com/media/26Ff5PmyrU5cNnGTC/giphy.gif",
            "https://media.giphy.com/media/3oKIPf3C7HqqYBVcCk/giphy.gif",
            "https://media.giphy.com/media/3ohzdYJK1wAdPWVk88/giphy.gif",
            "https://media.giphy.com/media/f9k1tV7HyORcngKF8v/giphy.gif",
            "https://media.giphy.com/media/1BXa2alBjrCXC/giphy.gif",
            "https://media.giphy.com/media/xT5LMtDrU29QaU3vWg/giphy.gif",
            "https://media.giphy.com/media/j5QcmXoFWl7jK/giphy.gif",
            "https://media.giphy.com/media/3orieZ3n6S3akU1TnW/giphy.gif",
            "https://media.giphy.com/media/26g8mf56a6D22/giphy.gif",
            "https://media.giphy.com/media/hjQIbgJb6ssOE/giphy.gif",
            "https://media.giphy.com/media/13gd6YVZ4wP3gm/giphy.gif",
            "https://media.giphy.com/media/l41lV7vd2rHDKMXK4/giphy.gif",
            "https://media.giphy.com/media/i1X1l9vXUzWy4/giphy.gif",
            "https://media.giphy.com/media/dXNkmwvoN5pqa/giphy.gif"
        ]

        # Calculate the countdown for 1 day
        time_remaining = datetime.timedelta(days=1)

        # Format the time remaining as a string (1 day in this case)
        countdown_message = f"⏰ Countdown: {time_remaining}"

        # Embed the joke and meme
        embed = discord.Embed(
            title="😂 Your daily unfunny dad joke!",
            description=f"{random.choice(jokes)}\n\n{countdown_message}",
            color=discord.Color.random()
        )
        embed.set_image(url=random.choice(meme_gifs))

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Funny(bot))
