from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# Setup Flask app
app = Flask('')

@app.route('/')
def home():
    return "✅ Web server is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Setup Discord bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Start Flask server and then bot
keep_alive()

try:
    token = os.environ['TOKEN']
    bot.run(token)
except KeyError:
    print("❌ TOKEN not found in environment variables!")
except Exception as e:
    print(f"❌ An error occurred: {e}")
