from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

keep_alive()
bot.run(os.environ['TOKEN'])  # Set your token in Replit Secrets or Render Environment
