import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")

bot.run("OTM3Mjc1MDIwNTc1NjQxNjMx.YfZXYg.JFAFIztftKdRLwfM0M7i3UO62Bg")