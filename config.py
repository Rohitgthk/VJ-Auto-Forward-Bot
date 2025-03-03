from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "1205c70ed6108fd639a84872bda21c9a")
      API_ID = int(getenv("API_ID", "26875163"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8090207974:AAEoUp_BHqbUDsETUwOEWkpRCLXEoUv4EZQ")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
