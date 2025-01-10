import os
import discord
import requests
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()
    print("Slash commands synced!")


@bot.tree.command(name="confess", description="Send an anonymous confession to the confessions channel!")
@app_commands.describe(content="Content of the message")
async def send(interaction: discord.Interaction, content: str):

    current_timestamp = datetime.now(timezone.utc).isoformat()

    data = {
        "username": "Anonymous Confessions",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Anonymous_emblem.svg/640px-Anonymous_emblem.svg.png",
        "embeds": [{
            "title": "Anonymous Confession",
            "description": content,
            "color": 0x3498db,
            "timestamp": current_timestamp
        }]
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        await interaction.response.send_message(f"Confession sent successfully!", ephemeral=True)
    else:
        await interaction.response.send_message(f"Failed to send confession. Error: {response.status_code}", ephemeral=True)

bot.run(BOT_TOKEN)
