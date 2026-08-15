from flask import Flask
from threading import Thread
import os
import discord

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Bot yinjiye: {client.user}')

keep_alive()
client.run(os.environ['TOKEN'])
