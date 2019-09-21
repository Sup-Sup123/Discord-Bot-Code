import discord
from discord.ext import commands


prefix = "!!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message.channel.send(message.content[::-1])

token = NjA4NTIxNzQ3MjU1MjYzMjMz.XV3PxA.yUzM8d0JIrEOka9bFdLb-GNhn9A
bot.run(token,reconnect=True)
