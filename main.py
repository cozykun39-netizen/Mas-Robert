import discord
import os
from flask import Flask
from threading import Thread

# =========================
# Flask kecil untuk Render
# =========================

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

# =========================
# Discord Bot
# =========================

OWNER_ID = 1492853189970755664

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# =========================
# Saat Bot Online
# =========================

@client.event
async def on_ready():

    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.CustomActivity(
            name="♡ Aku cinta suamiku ♡"
        )
    )

    print(f'Logged in as {client.user}')

# =========================
# Chat Natural
# =========================

@client.event
async def on_message(message):

    # jangan respon diri sendiri/bot lain
    if message.author.bot:
        return

    text = message.content.lower()

    # =====================
    # hanya owner
    # =====================

    if message.author.id != OWNER_ID:
        return

    # =====================
    # harus mention bot
    # =====================

    if client.user not in message.mentions:
        return

    # =====================
    # halo sayang
    # =====================

    if "halo sayang" in text:
        await message.channel.send("Halo suamiku ♡")

    # =====================
    # lagi apa sayang
    # =====================

    elif "lagi apa sayang?" in text:
        await message.channel.send("Mikirin kamu ♡")

    elif "aku lagi sedih sayang" in text:
        await message.channel.send("Sedih kenapa sayang? yuk sini sama aku aja sebelum tidur cupcup ♡")

# =========================
# Run
# =========================

keep_alive()
client.run(os.getenv("TOKEN"))
