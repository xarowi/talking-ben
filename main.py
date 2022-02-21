import discord
import os
from discord.ext.commands import Bot
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

bot = Bot(command_prefix='b>')
token = os.environ.get('DISCORD_TOKEN')
sessions = []

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


@bot.command()
async def join(ctx):
    try:
        await ctx.author.voice.channel.connect()

        embed = discord.Embed(title="Okay!", description="I'm connected to you and can speak with you.", color=0x66ff00)
        embed.set_footer(text="You're need to connect to any voice channel and try to invite me.")
        
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="I can't connect to your voice channel.", description="Because you're not a connected to any voice channel.", color=0x66ff00)
        embed.set_footer(text="You're need to connect to any voice channel and try to invite me.")

        await ctx.send(embed=embed)


@bot.command()
async def leave(ctx):
    for voice_client in bot.voice_clients:
        voice_channel = voice_client.channel

        if ctx.message.channel.guild == voice_channel.guild:
            await voice_client.disconnect()

            embed = discord.Embed(title="Okay!", description="I leaved from voice channel. Have a good day.", color=0x66ff00)
            embed.set_footer(text="Good luck!")

            return await ctx.send(embed=embed)
    
    embed = discord.Embed(title="I can't leave from voice channel.", color=0x66ff00)
    embed.set_footer(text="I don't know what to say, lol!")

    await ctx.send(embed=embed)

bot.run(token)
