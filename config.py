from dotenv import dotenv_values

config = dotenv_values(".env")

TELEGRAM_TOKEN = config["8063343257:AAGNlU05pOaNLkyPDqaPKtDw47hK6PadItU"]
OPENROUTER_KEY = config["OPENROUTER_KEY"]
NEUROIMG_KEY = config["NEUROIMG_KEY"]
