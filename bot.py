import os
import random
import typing
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# get the quotes
QUOTES_URL = "https://raw.githubusercontent.com/pognog69/tingfeng-discord/master/quotes.txt"
quotes = []
for line in requests.get(QUOTES_URL, stream=True).iter_lines(decode_unicode=True):
    if line: quotes.append(line)


# big boy initialization
bot = commands.Bot(command_prefix='tf ')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# quote command
@bot.command(name='quote', help='If a number is given (e.g. tf quote 69), displays that quote. Else, displays a random Ting Feng quote')
async def random_quote(ctx, id: typing.Optional[int] = -1):

    if id < 1 or id > len(quotes):
        id = random.randrange(1, len(quotes)+1)

    quote = quotes[id-1]

    embed = discord.Embed(color=0x6b8e23)
    embed.add_field(name=f'\\#{id}', value=quote, inline=True)
    embed.set_footer(text='-Ting Feng')

    await ctx.send(embed=embed)


bot.run(TOKEN)
