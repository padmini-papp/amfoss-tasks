# Berry Broker - Dank Memer style Discord Bot

This is my Discord bot for Task 07. Its a fake pirate economy bot, kind of like Dank Memer but One Piece themed. Every member of the server is treated like a pirate, they start with some berries (the currency), and can earn more, gamble it away, or steal from other people using different commands.

## Commands

!bounty - check your current berry balance
!setsail - claim your daily berries (once every 24 hours)
!trade @user <amount> - send berries to someone else
!duel <rock/paper/scissors> - bet 50 berries in a rock paper scissors against the bot
!raid @user - try to steal berries from someone, 50% chance of success, has a 1 hour cooldown
!roast @user - sends a random insult at someone
!worstgeneration - shows the top 5 richest users on the server
!logpose - pulls a random character's info from the One Piece API

## How to run it

1. Clone this repo
2. Make a virtual environment: python3 -m venv venv
3. Activate it: source venv/bin/activate
4. Install the required packages: pip install discord.py python-dotenv aiohttp
5. Make a .env file and put your bot token in it like this: DISCORD_TOKEN=your_token_here
6. Run it: python3 bot.py

## File structure

bot.py - main file, connects to discord and loads the cogs
database.py - handles all the sqlite database stuff
cogs/economy.py - bounty, setsail, trade commands
cogs/games.py - duel, raid commands
cogs/fun.py - roast, worstgeneration, logpose commands
.env - has my bot token, not pushed to github
.gitignore - ignores venv and .env

## Database

Uses sqlite (bot.db), one table called users:
- user_id - discord id of the user, primary key
- username - their discord username
- balance - how many berries they have
- last_daily - when they last used setsail, for the cooldown
- last_rob - when they last used raid, for the cooldown
