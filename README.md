# DiscordBot
Discord bot, that controls PiRelay V2
## Installation
```
pip3 install -r requirements.txt

python3 bot.py
```
## Running as a Linux service
```
sudo cp discordbot.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl start discordbot.service
```
# Usage example
Send "relay 1 on" to your discord bot and it answers with relay 1 on
