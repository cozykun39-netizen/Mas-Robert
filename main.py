import discord
import os

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.CustomActivity(name="watching silently...")
    )
    print(f'Logged in as {client.user}')

client.run(os.getenv("TOKEN"))
