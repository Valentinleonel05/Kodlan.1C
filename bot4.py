import discord
from discord.ext import commands
import asyncio 
asyncio.set_event_loop(asyncio.new_event_loop())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    

reciclables = ["Plastico", "Carton", "Vidrio", "Papel", "Lata"]
no_reciclables = ["Papel sucio", "Panales", "Colillas", "Ceramica", "Espejos"]

@bot.command()
async def lista(ctx):
    X = ""
    for i in reciclables:
        X += i +", "
    Y = ""
    for G in no_reciclables:
        Y += G + ", "
    await ctx.send(f"Reciclables {X}")
    await ctx.send(f"No Reciclables {Y}") 


bot.run("MTUxMTE0MDQzOTYzMjI0ODg5NA.GftCMD.PaPzCkQSYXFMJFeTMbIyqlVsbAUcDFLVnilrfw")