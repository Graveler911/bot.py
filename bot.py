import discord
from discord.ext import commands

per = discord.Intents.default()
per.message_content=True

bot=commands.Bot(command_prefix="/",intents=per)

@bot.event
async def on_ready():
    print(f"El bot {bot.user} esta vivo")
@bot.command()
async def des(ctx,*,objeto:str):
    listdesc ={
        "botella de plastico": 500,
        "chicle": 10,
        "vidrio": 5000
    }
    objeto=objeto.lower()
    if objeto in listdesc:
        await ctx.send(f"el obejto {objeto} tarda en descomponerse {listdesc[objeto]} años" )
    else:
        await ctx.send(f"el {objeto} no esta en mi base de datos" )

bot.run("your token ")
