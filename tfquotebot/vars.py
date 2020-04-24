import os
from dotenv import load_dotenv
from requests import get


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


QUOTES_URL = "https://raw.githubusercontent.com/pognog69/tingfeng-discord/master/quotes.txt"


def getQuotes():
    quotes = []
    for line in get(QUOTES_URL, stream=True).iter_lines(decode_unicode=True):
        if line:
            quotes.append(line)
    return quotes
