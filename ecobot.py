import discord
from discord.ext import commands
from datetime import datetime as dt
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Mi chiamo Giampiero Peppino Gianfranco e sono qui per aiutarti a risolvere il problema dell\' inquinamento {bot.user}!')
infos = [
    "Quando vengono lanciati razzi ad alta tecnologia, vengono rilasciate nell'atmosfera enormi quantità di sostanze inquinanti.",
    "La produzione di batterie per auto ecologiche senza pilota non è così ecologica.",
    "Molti oggetti sono fatti di plastica che impiega centinaia di anni per decomporsi!"
]
info2 = []
@bot.command()
async def info(ctx):
    global infos, info2
    n = len(infos)
    i = random.randint(0, n-1)
    inf=infos.pop(i)
    await ctx.send(inf)
    info2.append(inf)
    if not infos:
        infos = info2
        info2 = []
    print(info2, infos)


bot.run("")