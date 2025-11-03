import discord
from discord.ext import commands
import PiRelay
from dotenv import load_dotenv
from cli_1 import cli_1
import os
import time

"""
# Your bot token
#TOKEN=
# User id of user who is authorized to command the bot
#AUTHORIZED_USER_ID = 
"""

# Loads TOKEN and AUTHORIZED_USER_ID from .env file
load_dotenv()
TOKEN = str(os.getenv('BOT_TOKEN'))
AUTHORIZED_USER_ID = int(os.getenv('AUTHORIZED_USER_ID'))

# Relay initialization using PiRelay labels
r1 = PiRelay.Relay("RELAY1")
r2 = PiRelay.Relay("RELAY2")
r3 = PiRelay.Relay("RELAY3")
r4 = PiRelay.Relay("RELAY4")

# Mapping relay names to objects
relay_map = {
    'relay 1': r1,
    'relay 2': r2,
    'relay 3': r3,
    'relay 4': r4
}

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.id != AUTHORIZED_USER_ID:
        return

    content = message.content.strip().lower()

    for relay_name, relay_obj in relay_map.items():
        if content == f"{relay_name} on":
            relay_obj.on()
            await message.channel.send(f"✅ {relay_name.title()} turned ON.")
            return
        elif content == f"{relay_name} off":
            relay_obj.off()
            await message.channel.send(f"✅ {relay_name.title()} turned OFF.")
            return

bot.run(TOKEN)
