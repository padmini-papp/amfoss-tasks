import discord
from discord.ext import commands
import random
import datetime
import database


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def duel(self, ctx, choice: str = None):
        options = ["rock", "paper", "scissors"]
        if choice is None or choice.lower() not in options:
            await ctx.send("Choose one: rock, paper, or scissors. Usage: `!duel rock`")
            return

        choice = choice.lower()
        bot_choice = random.choice(options)
        user_id = str(ctx.author.id)
        database.get_user(user_id, str(ctx.author))

        bet = 50

        if choice == bot_choice:
            result = "It's a draw! No Berries lost."
        elif (
            (choice == "rock" and bot_choice == "scissors") or
            (choice == "paper" and bot_choice == "rock") or
            (choice == "scissors" and bot_choice == "paper")
        ):
            database.update_balance(user_id, bet)
            result = f"You win! +{bet} Berries."
        else:
            database.update_balance(user_id, -bet)
            result = f"You lose! -{bet} Berries."

        await ctx.send(f"⚔️ You chose **{choice}**, I chose **{bot_choice}**. {result}")

    @commands.command()
    async def raid(self, ctx, member: discord.Member):
        raider_id = str(ctx.author.id)
        target_id = str(member.id)

        if raider_id == target_id:
            await ctx.send("You can't raid yourself, Captain.")
            return

        now = datetime.datetime.now()
        raider = database.get_user(raider_id, str(ctx.author))
        last_rob = raider[4]

        if last_rob is not None:
            last_time = datetime.datetime.fromisoformat(last_rob)
            if now - last_time < datetime.timedelta(hours=1):
                remaining = datetime.timedelta(hours=1) - (now - last_time)
                minutes = remaining.seconds // 60
                await ctx.send(f"⏳ Your crew needs to rest. Try again in {minutes}m.")
                return

        target = database.get_user(target_id, str(member))

        success = random.random() < 0.5

        database.set_last_rob(raider_id, now.isoformat())

        if success and target[2] > 0:
            stolen = min(100, target[2])
            database.update_balance(raider_id, stolen)
            database.update_balance(target_id, -stolen)
            await ctx.send(f"🏴‍☠️ Raid successful! You stole **{stolen} Berries** from {member.mention}.")
        else:
            penalty = 50
            database.update_balance(raider_id, -penalty)
            await ctx.send(f"💥 Raid failed! You lost **{penalty} Berries** trying to raid {member.mention}.")


async def setup(bot):
    await bot.add_cog(Games(bot))