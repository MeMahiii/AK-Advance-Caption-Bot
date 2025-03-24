from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7338196784"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://files.catbox.moe/9zv22s.jpg")
API_ID = int(getenv("API_ID", "21316774"))
API_HASH = str(getenv("API_HASH", "50f64c71c78a34a85dad33fb78fc6c33)
BOT_TOKEN = str(getenv("BOT_TOKEN", "7508114207:AAHSgrtvNsFhulIdFVQczsna_Saz9vUSKY4"))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002408300116") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://Filterbot:wywgsgwwwuww2iqiw@cluster0.s7cys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
