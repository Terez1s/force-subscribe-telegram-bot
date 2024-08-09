import os

class Config():
    ENV = bool(os.environ.get('ENV', False))
    
    if ENV:
        BOT_TOKEN = os.environ.get("BOT_TOKEN", "6851857209:AAFduiamnzMN779iLdOSlmEKrK3-ijGOZIM")
        DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Terez2:Suldan@cluster0.7czxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        APP_ID = int(os.environ.get("APP_ID", 19867363))
        API_HASH = os.environ.get("API_HASH", "c39149b542ef84337e65c6ec6dc07bd3")
        SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1998605919").split()))
        SUDO_USERS.append(939425014)  # Adding a specific Sudo user
        SUDO_USERS = list(set(SUDO_USERS))
    else:
        BOT_TOKEN = "6851857209:AAFduiamnzMN779iLdOSlmEKrK3-ijGOZIM"
        DATABASE_URL = "mongodb+srv://Terez2:Suldan@cluster0.7czxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        APP_ID = 19867363
        API_HASH = "c39149b542ef84337e65c6ec6dc07bd3"
        SUDO_USERS = [1998605919, ]  # Default Sudo users

class Messages():
    HELP_MSG = [
        ".",
        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        "**Commands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn off ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        "**Developed by @Terez1s**"
    ]

    START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
