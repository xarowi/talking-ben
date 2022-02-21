import discord
import os
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

bot = Bot(command_prefix='b>')
token = os.environ.get('DISCORD_TOKEN')

bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Talking Ben! have logged in as {bot.user}!")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Hello, i'm a Talking Ben!",
                          description="You can invite me to voice channel and talk with me!", color=0x66ff00)

    embed.set_thumbnail(
        url="https://yt3.ggpht.com/a/AGF-l7_8VDwnT0jSLc-tymVClu7vovheaVCq5z8tmQ=s900-c-k-c0xffffffff-no-rj-mo")

    embed.add_field(
        name="b>join", value="Join to your voice channel!", inline=True)
    embed.add_field(name="b>call", value="Call to my telephone!", inline=True)
    embed.add_field(
        name="b>leave", value="Leave from voice channel!", inline=True)

    embed.set_footer(text="Created by поно#7361")
    await ctx.send(embed=embed)

bot.run(token)
