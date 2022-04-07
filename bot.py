import discord
from discord.ext import commands
import platform
import psutil
import uptime
import datetime
import random
import time
import os
import json
import requests
import asyncio

intents = discord.Intents.all()
intents.members = True
intents.presences = True

Client = discord.Client()
client = commands.Bot(command_prefix = "!", intents = intents)
client.remove_command('help')


@client.event
async def on_ready():
    print("BOT ONLINE")
 
 
@client.event
async def on_message(ctx):
    await client.process_commands(ctx)
 
@client.slash_command(
    name = "bot_info",
    description= "Command to display information about the bot.",
    guild_ids = [960288719871569961]
)
async def bot_info(ctx):
    value = random.randint(0, 0xffffff)
    system = platform.system()
    architecture = platform.machine()
    release = platform.release()
    sys_version = platform.version()
    cpu_percent = psutil.cpu_percent()

    if os.name == 'nt':
        uptime_sys = uptime._uptime_windows()
    elif os.name == 'posix':
        uptime_sys = uptime._uptime_linux()

    mem_total = psutil.virtual_memory()[0]
    mem_used = psutil.virtual_memory()[3]

    info = discord.Embed(
    colour = value
    )

    info.set_author(name="Bot Statistics")
    info.add_field(name="System", value=system + " " + architecture + " " + release)
    info.add_field(name="System Version", value=sys_version)
    info.add_field(name="CPU Usage", value=str(cpu_percent) + "%")
    info.add_field(name="RAM Usage", value=str(int(mem_used / 1024 / 1024)) + "MB" + " / " + str(int(mem_total / 1024 / 1024)) + "MB")
    info.add_field(name="Uptime", value=str(datetime.timedelta(seconds=round(uptime_sys))))
    info.set_footer(text=f'Requested by {ctx.author}')
    
    await ctx.respond(embed=info)

    

client.run("")
