import os
import requests
import discord
from dotenv import load_dotenv

QUOTES_URL = "https://raw.githubusercontent.com/pognog69/tingfeng-discord/master/quotes.txt"
quotesRequest = requests.get(QUOTES_URL, stream=True)
quotes = []
for line in quotesRequest.iter_lines(decode_unicode=True):
    if line:
        quotes.append(line)
print(quotes)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()
