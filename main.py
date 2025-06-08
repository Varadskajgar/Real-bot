from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# === Flask Web Server to Keep Alive ===
app = Flask('')

@app.route('/')
def home():
    return "✅ Web server is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run).start()

# === Discord Bot Setup ===
intents = discord.Intents.default()
intents.message_content = True  # Required to respond to messages

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# === Start Everything ===
keep_alive()

try:
    token = os.environ['TOKEN']
    bot.run(token)
except KeyError:
    print("❌ TOKEN not set in environment variables!")
except Exception as e:
    print(f"❌ Error: {e}")
