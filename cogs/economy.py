import discord
from discord.ext import commands
import datetime
import database


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bounty(self, ctx):
        user = database.get_user(str(ctx.author.id), str(ctx.author))
        balance = user[2]
        await ctx.send(f"🏴‍☠️ {ctx.author.mention}, your bounty is **{balance} Berries**.")

    @commands.command()
    async def setsail(self, ctx):
        user_id = str(ctx.author.id)
        username = str(ctx.author)
        user = database.get_user(user_id, username)

        now = datetime.datetime.now()
        last_daily = user[3]

        if last_daily is not None:
            last_time = datetime.datetime.fromisoformat(last_daily)
            if now - last_time < datetime.timedelta(hours=24):
                remaining = datetime.timedelta(hours=24) - (now - last_time)
                hours = remaining.seconds // 3600
                await ctx.send(f"⏳ You already raided today! Come back in {hours}h.")
                return

        reward = 200
        database.update_balance(user_id, reward)
        database.set_last_daily(user_id, now.isoformat())
        await ctx.send(f"⚓ You raided a merchant ship at dawn and earned **{reward} Berries**!")

    @commands.command()
    async def trade(self, ctx, member: discord.Member, amount: int):
        sender_id = str(ctx.author.id)
        receiver_id = str(member.id)

        if amount <= 0:
            await ctx.send("You must trade a positive amount.")
            return

        sender = database.get_user(sender_id, str(ctx.author))
        if sender[2] < amount:
            await ctx.send("You don't have enough Berries for that trade.")
            return

        database.get_user(receiver_id, str(member))
        database.update_balance(sender_id, -amount)
        database.update_balance(receiver_id, amount)
        await ctx.send(f"💰 {ctx.author.mention} traded **{amount} Berries** to {member.mention}.")


async def setup(bot):
    await bot.add_cog(Economy(bot))