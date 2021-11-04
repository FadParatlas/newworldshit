import os

import discord
import random
from checkwebsite import findserverstatus
from discord.ext import commands, tasks

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@tasks.loop(seconds=5.0)
async def check_status_online():

    channel = client.get_channel(899396765302816769)
    status = findserverstatus()
    if status == 'Online':
        return
    else:
        await channel.send(status)
        check_status_online.cancel()
        check_status_offline.start()

@tasks.loop(seconds=5.0)
async def check_status_offline():

    channel = client.get_channel(899396765302816769)
    status = findserverstatus()

    if status != 'Online':
        return
    else:
        await channel.send(status)
        check_status_offline.cancel()
        check_status_online.start()


@check_status_online.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'. format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'debug':
        if user_message.lower() =='hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() =='bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'this is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return
        if user_message.lower() =='checkstatus':
            status = findserverstatus()
            await message.channel.send('Erythia is ' + status)

check_status_online.start()
client.run(TOKEN)
