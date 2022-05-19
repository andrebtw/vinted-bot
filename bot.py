from ast import arg
import numbers
import discord
from discord.ext import commands
from discord.commands import Option
import platform
import psutil
import uptime
import datetime
import random
import time
import os
import asyncio
import json
import requests
from re import I
from pyVinted import Vinted

vinted = Vinted("fr")


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

@client.slash_command(
    name = "vinted",
    description= "Rechercher sur Vinted. (Une commande test)",
    guild_ids = [960288719871569961]
)
async def vinted_search(
    ctx,
    arg1: Option(str, "Option 1", required = False, default=""),
    arg2: Option(str, "Option 2", required = False, default="")
    ):
    running = True
    price = 9999
    while running:
        number_of_items = 200
        page = 1
        items = vinted.items.search(f"https://www.vinted.fr/?order=newest_first&price_to={price}&currency=EUR", number_of_items, page)

        items_d = []
        for i in items:
            items_d.append(i)
        
        print(f"Items found : {len(items_d)}")

        a=0

        for i in items_d:
            if (arg1 in i.url or (arg1 is None and arg2 is None)):
                a=a+1
                print(f"Items selected : {a}")

        for i in items_d:
            try:
                if (arg1 in i.url or (arg1 is None and arg2 is None)):
                    value = random.randint(0, 0xffffff)
                    info = discord.Embed(title=i.title, url=i.url, colour = value)
                    info.set_thumbnail(url=i.photo)
                    info.add_field(name=f"Marque", value=f"{i.brand_title}")
                    info.add_field(name=f"Prix", value=f"{i.price}€")
                    info.set_footer(text=f'ID du produit : {i.id}')
                    await ctx.respond(embed=info)
                    await asyncio.sleep(2)
            except:
                pass

token = open("token.txt", "r")

client.run(token.read())