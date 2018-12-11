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
    await ctx.send("```css
Ainda nao temos ip!```")

bot.run('NTIyMDc4NzU4NDUxMjgxOTIx.DvFy2A.yuqHZvNIVVJ6h-jRRA-wJ6QOXLg')
