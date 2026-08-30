import discord
from discord.ext import commands
import random
import aiohttp
import database

ROASTS = [
    "You're about as useful as a chocolate anchor.",
    "Even Buggy the Clown has a better crew than you.",
    "Your bounty poster is used as toilet paper in Marine HQ.",
    "You call that a sword? My grandma peels fruit sharper.",
    "You'd get lost sailing across a puddle.",
]


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roast(self, ctx, member: discord.Member):
        line = random.choice(ROASTS)
        await ctx.send(f"🔥 {member.mention}, {line}")

    @commands.command()
    async def worstgeneration(self, ctx):
        top_users = database.get_top_users(5)
        if not top_users:
            await ctx.send("No pirates have earned a bounty yet.")
            return

        lines = []
        for i, (username, balance) in enumerate(top_users, start=1):
            lines.append(f"**{i}.** {username} — {balance} Berries")

        message = "👑 **Worst Generation Leaderboard** 👑\n" + "\n".join(lines)
        await ctx.send(message)

    @commands.command()
    async def logpose(self, ctx):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://api.api-onepiece.com/v2/characters/en") as resp:
                    if resp.status != 200:
                        await ctx.send("The Log Pose spins wildly... the signal is lost at sea.")
                        return
                    data = await resp.json()
                    character = random.choice(data)
                    name = character.get("name", "Unknown pirate")
                    bounty = character.get("bounty", "Unknown")
                    await ctx.send(f"🧭 The Log Pose points to **{name}**! Bounty: {bounty}")
            except Exception:
                await ctx.send("The Log Pose spins wildly... the signal is lost at sea.")


async def setup(bot):
    await bot.add_cog(Fun(bot))