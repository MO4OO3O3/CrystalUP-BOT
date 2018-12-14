import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ip(ctx):
    await ctx.send("```O servidor ira ser aberto em 25/12```")

@bot.command()
async def afonso(ctx):
    await ctx.send("`I'm afonso and i'm gay`")

@bot.command()
async def projetos(ctx):
    await ctx.send("Meus Projetos:")
    await ctx.send("https://www.youtube.com/watch?v=8Y0j7v8ty_0")
    await ctx.send("```No futuro irei adicionar mais!```")
    
@bot.command()
async def nodi(ctx):
    await ctx.send("Amo-te Nodi")
    await ctx.send("https://www.youtube.com/watch?v=iY-BC-NqDSI")
    
@bot.command()
async def dinheiro(ctx):
    await ctx.send("`INFO`)
    await ctx.send("`Porquinho para pagar a Host`")
    await ctx.send("``00/10€``")
    await ctx.send("`Caso queiras Doar`")
    await ctx.send("https://www.paypal.me/crystalup")
    
    
bot.run('NTIyMDc4NzU4NDUxMjgxOTIx.DvWmjQ.32cOZwPOsw-dvqI0sbYVtArYMOo')
