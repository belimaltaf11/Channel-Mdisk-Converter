import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "29081699"))
API_HASH = os.environ.get("API_HASH", "4c4beb5bf57a6d52a4cda249a98f0980")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6233366267:AAF9Jxt2eAU6CBnk4Zp1mlk7kxSOc8o2ics")
DROPLINK_API = os.environ.get("DROPLINK_API", "d65c658c53d5cf2849f0a004124c18fc80642151")
MDISK_API = os.environ.get("MDISK_API", "1QYeNzQTxPxUwmIT8Hvb")
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertorBotpro")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://short:sh9824786@cluster0.szric3m.mongodb.net/?retryWrites=true&w=majority")
WEBSITE = os.environ.get('WEBSITE', 'https://url.staus.in')

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(",")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "True")), True)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/Dkmovie/Channel-Mdisk-Converter")
USERNAME = os.environ.get("USERNAME", "movie_a1")
HEADER_TEXT = os.environ.get("HEADER_TEXT", '')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", '')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False
