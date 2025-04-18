import discord
from discord.ext import commands
from colorama import Fore, Style

# Set up the bot
bot = commands.Bot(command_prefix="!")

# When the bot is ready
@bot.event
async def on_ready():
    print(Fore.GREEN + f'Logged in as {bot.user}' + Style.RESET_ALL)

# A simple command that responds with a colorful and enhanced message
@bot.command()
async def hello(ctx):
    embed = discord.Embed(
        title="Hello, World!", 
        description="This is a colorful response from your bot!", 
        color=discord.Color.blue()
    )
    embed.add_field(name="Greetings!", value="Hello, *{0}*!".format(ctx.author.name), inline=False)
    embed.set_footer(text="Enjoy the colors!")
    
    # Send the embed message
    await ctx.send(embed=embed)

# Run the bot
bot.run("YOUR_BOT_TOKEN")
