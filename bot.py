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
    
    
bot.run('NTIyMDc4NzU4NDUxMjgxOTIx.DvFy2A.yuqHZvNIVVJ6h-jRRA-wJ6QOXLg')
