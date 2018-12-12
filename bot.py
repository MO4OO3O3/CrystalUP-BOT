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
    await ctx.send("`Ainda nao temos ip!`")

@bot.command()
async def afonso(ctx):
    await ctx.send("`I'm afonso and i'm gay`")

@bot.command()
async def projetos(ctx):
    await ctx.send("Meus Projetos:")
    await ctx.send("https://gamersboard.com.br/topic/63623-morais-minas-ganhe-dinheiro-ao-minerar/")
    await ctx.send("")
    await ctx.send("No futuro irei adicionar mais!")
    
    
bot.run('NTIyMDc4NzU4NDUxMjgxOTIx.DvFy2A.yuqHZvNIVVJ6h-jRRA-wJ6QOXLg')
