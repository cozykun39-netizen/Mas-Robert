import discord
import os
from flask import Flask
from threading import Thread

# Flask app kecil
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# Discord bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle
        activity=discord.CustomActivity(name="♡ Aku cinta suamiku♡ ")
    )
    print(f'Logged in as {client.user}')

keep_alive()
client.run(os.getenv("TOKEN"))
