import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

QUOTES_URL = "https://raw.githubusercontent.com/pognog69/tingfeng-discord/master/quotes.txt"
quotes = []
for line in requests.get(QUOTES_URL, stream=True).iter_lines(decode_unicode=True):
    if line: quotes.append(line)

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
