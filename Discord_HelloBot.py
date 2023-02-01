import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from discord.ext.commands import CommandNotFound

##host = "dpg-ce6kvoen6mpk2bmk0db0-a.oregon-postgres.render.com"
##user = "taejun"
##password = "PVLf75Wu9epD4MRQ9lG69NXa0Hw0eamE"
##database = "taejundb"
##port_db = "5432"


discord_token = "MTA2OTg1MDcxMDgwMTM5OTgyOA.GZzP1v.yNz4JUhZtemCbAPagldRx4ZDibSLPZjeBJ6KgU"


intents = discord.Intents.all()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix = '$ ', intents=intents)


@client.event
async def on_ready():
    print('Bot name: {}'.format(client.user.name))  
    print('Bot ID: {}'.format(client.user.id)) 


@client.event
async def on_message(message):
    
    content = message.content
    user = message.author
    channel = message.channel


    print(content)
    print(user)
    print(channel)
    if message.author == client.user:
        return

    elif message.content.startswith('hello'):
        await message.channel.send("Hello! "+str(user))


client.run(discord_token)
