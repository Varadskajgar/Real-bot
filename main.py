from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

app = Flask('')

@app.route('/')
def home():
    return "✅ Web server is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

keep_alive()

try:
    token = os.environ['TOKEN']
    bot.run(token)
except KeyError:
    print("❌ TOKEN not set in environment variables!")
except Exception as e:
    print(f"❌ Error: {e}")
