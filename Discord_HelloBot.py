import discord
import os
import TJ_DBConnection 
import User
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from discord.ext.commands import CommandNotFound
from pytz import timezone


# 사용자별 채팅, 음성을 모조리 기록해서 
# DB에 저장하고 
# 한 달에 한 번 인원정리를 하는데,
# 특정 음성채널 입장 누적 시간이 1시간 미만인 
# 사람들을 걸러내는 봇 쓰고있어
# 내가 지금 만들어놓은건 버그도 많은 것 같고 
# 코드 정리1도 안 되어 있어서 

discord_token = "MTA2OTg1MDcxMDgwMTM5OTgyOA.GZzP1v.yNz4JUhZtemCbAPagldRx4ZDibSLPZjeBJ6KgU"

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix = '$ ', intents=intents)

TJ_DBConnection.DBConnection.dbconn()
# TJ_DBConnection.DBConnection.getAllUser()

@client.event
async def on_ready():
    print('Bot name: {}'.format(client.user.name))  
    print('Bot ID: {}'.format(client.user.id)) 


@client.event
async def on_message(message):
    
    content = message.content
    user = message.author
    channel = message.channel
    guild = channel.guild

    current_timezone_time = message.author.joined_at
    new_timezone_time = current_timezone_time.astimezone(timezone('Asia/Seoul'))
    print(new_timezone_time)
    print(User.getUser(user))
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
