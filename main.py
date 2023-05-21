import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if random.random() <= 0.05:
        letras = ["a", "e","a","i","j","a","i","j","j","a","i","j","a", "i", "u", "j", "k", "h"]
        risa = ''.join(random.choice(letras) for _ in range(random.randint(10, 25)))
        await message.channel.send(risa)
    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
