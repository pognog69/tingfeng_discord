__version__ = '0.1.0'
from .bot import bot
from .vars import DISCORD_TOKEN


# poetry run tfquotebot
def main():
    bot.run(DISCORD_TOKEN)
