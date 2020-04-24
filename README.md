# tingfeng-discord

Ting Feng Quotes Discord bot

:b: :b: :b: Visit [our website](https://xn--137h.ga) for more information. :b: :b: :b:

### """Build""" instructions

The bot does not function unless a `.env` [file](https://pypi.org/project/python-dotenv/) containing the line `DISCORD_TOKEN=ReplaceThisWithYourToken` exists in the same directory as the script with your application's token substituted for the value of `DISCORD_TOKEN`.

First you'll need Python 3.8.2 and the [poetry](https://python-poetry.org/) package. You can install it with `pip` or `pipx` or, if you're on a Mac, `brew` has it as well. Then just `cd /path/to/tingfeng-discord` and run `poetry install` to install the dependencies to the environment. After that do `poetry run python bot.py` (until I figure out how to builds lol) and the bot will come online in servers you've added it to.
