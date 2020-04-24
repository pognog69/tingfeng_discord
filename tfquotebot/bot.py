#      _______ _               ______
#     |__   __(_)             |  ____|
#        | |   _ _ __   __ _  | |__ ___ _ __   __ _
#        | |  | | '_ \ / _` | |  __/ _ \ '_ \ / _` |
#        | |  | | | | | (_| | | | |  __/ | | | (_| |
#        |_|  |_|_| |_|\__, | |_|  \___|_| |_|\__, |
#                       __/ |                  __/ |
#                      |___/                  |___/
#
#                                ...is still single!

from random import randrange
from typing import Optional
import discord
from discord.ext.commands import Bot
from .vars import getQuotes

# big boy initialization
bot = Bot(command_prefix='tf ', activity=discord.Game(name='tf help'))
@bot.event
async def on_ready():
    print(f'{bot.user.name} ID {bot.user.id} has connected to Discord!')


# quote command
@bot.command(name='quote', help='If a number is given (e.g. tf quote 69), displays that quote. Else, displays a random Ting Feng quote')
async def random_quote(ctx, id: Optional[int] = -1):

    quotes = getQuotes()
    if id < 1 or id > len(quotes):
        id = randrange(1, len(quotes)+1)

    quote = quotes[id-1]

    embed = discord.Embed(color=0x6b8e23)
    embed.add_field(name=f'\\#{id}', value=quote, inline=True)
    embed.set_footer(text='-Ting Feng')

    await ctx.send(embed=embed)
