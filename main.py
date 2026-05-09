import discord
import os
from flask import Flask
from threading import Thread
from discord.ext import commands

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

OWNER_ID = 1492853189970755664  # GANTI DENGAN USER ID KAMU

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="halo", intents=intents)

# Saat bot online
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.CustomActivity(
            name="♡ Aku cinta suamiku ♡"
        )
    )

    print(f'Logged in as {bot.user}')

# =========================
# Command khusus owner
# =========================

@bot.command()
async def sayang(ctx):

    if ctx.author.id != OWNER_ID:
        await ctx.send("Maaf kamu bukan suamiku, aku malas jawab")
        return

    await ctx.send("Halo suamiku ♡")

# Command ganti status
@bot.command()
async def status(ctx, *, text):

    if ctx.author.id != OWNER_ID:
        return

    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.CustomActivity(name=text)
    )

    await ctx.send(f'Status diubah menjadi: {text}')

# =========================
# Run
# =========================

keep_alive()
bot.run(os.getenv("TOKEN"))
