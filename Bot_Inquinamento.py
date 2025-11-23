import discord
from discord.ext import commands
from inquinamento import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao!")

@bot.command()
async def aiuto(ctx):
    testo = """> Ti diamo il **benvenuto** nel bot ***Anti-Inquinamento***
> Questa è la sezione *aiuto*.
>               - `$dove`: con questo comando puoi digitare il tuo **rifiuto** e ricevere una guida di dove buttare la spazzatura"""
    await ctx.send(testo)

@bot.command()
async def dove(ctx, *, rifiuto: str):
    risposta = consiglio(rifiuto)
    await ctx.send(risposta)

bot.run("TOKEN")
