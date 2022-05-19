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
                            price: Option(int, "Le prix maximum", required = False, default = 500),
                            arg1: Option(str, "Option 1", required = False, default=""),
                            arg2: Option(str, "Option 2", required = False, default="")
                        ):
    number_of_items = 40
    page = 1

    # search (url, number of items, page_number)
    items = vinted.items.search(f"https://www.vinted.fr/?order=newest_first&price_to={price}&currency=EUR", number_of_items, page)

    # returns a list of objects : item

    # Getting all the 10 items into a list
    items_d = []
    for i in items:
        items_d.append(i)
    
    items_selected = []

    for i in items_d:
        if arg1 in i.url:
            items_selected.append(i)

    item1 = items_selected[0]

    # title
    item1.title

    # id
    item1.id

    # photo url
    item1.photo

    # brand title
    item1.brand_title

    # price
    item1.price

    # url
    item1.url

    # currency
    item1.currency


    # Reply
    value = random.randint(0, 0xffffff)

    info = discord.Embed(title=item1.title, url=item1.url, colour = value
    )

    #info.set_author(name=item1.brand_title)
    info.set_thumbnail(url=item1.photo)
    info.add_field(name=f"Marque", value=f"{item1.brand_title}")
    info.add_field(name=f"Prix", value=f"{item1.price}€")
    info.set_footer(text=f'ID du produit : {item1.id}')
    await ctx.respond(embed=info)

token = open("token.txt", "r")

client.run(token.read())