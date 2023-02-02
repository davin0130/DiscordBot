import discord
import os
import TJ_DBConnection 
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from discord.ext.commands import CommandNotFound


discord_token = "MTA2OTg1MDcxMDgwMTM5OTgyOA.GZzP1v.yNz4JUhZtemCbAPagldRx4ZDibSLPZjeBJ6KgU"

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix = '$ ', intents=intents)

TJ_DBConnection.DBConnection()


@client.event
async def on_ready():
    print('Bot name: {}'.format(client.user.name))  
    print('Bot ID: {}'.format(client.user.id)) 


@client.event
async def on_message(message):
    
    content = message.content
    user = message.author
    channel = message.channel
    guild = message.channel.guild

    if user == client.user:
        return

    elif content.startswith('hello'):
        await channel.send("Hello! "+str(user))

    elif content == "$user":
        member_num = 0
        to_send_users = f'서버명 [{guild.name}]: 멤버 [{guild.member_count}명]\n\n'
        for member in guild.members:
            member_num += 1
            to_send_users += f'{member_num}. {member}\n'
        await channel.send(to_send_users)
    
    elif content == "$채팅기록":
        chat_log = f'{user} | {content}'
        await channel.send(chat_log)

client.run(discord_token)


#===================================================================

##@bot.event
##async def on_ready():
##    print('Bot name: {}'.format(bot.user.name))  
##    print('Bot ID: {}'.format(bot.user.id)) 
##
##@bot.command()
##async def ping(ctx):
##    print(ctx)
##    await ctx.channel.send("pong")
##
##
##bot.run(discord_token)
