# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! '+message.author.mention)
        return

    if message.content.startswith('$laughat'):
        user = message.mentions
        await message.channel.send(user[0].mention + ' <:kek:782113232848289842>')
        return

    if '69' in message.content:
        user = message.mentions
        await message.channel.send('nice')
        return

    if 'lulw' in message.content:
        await message.channel.send('I think you meant kekw <:kek:782113232848289842>')
        return

    if message.content.startswith('$emojis'):
        if len(message.channel.guild.emojis) == 0:
            await message.channel.send('This server has no custom emojis')
        for emoji in message.guild.emojis:
            await message.channel.send(emoji)
        return

    if 'uwu' in message.content or 'UWU' in message.content:
        await message.channel.send('UWU')
        return

    if message.content.startswith('im ') or message.content.startswith('i’m ') or message.content.startswith('I’m '):
        await message.channel.send('Hi ' + message.content.split(' ', 1)[1])
        return

    brooklyn_99_quotes = [ 'Luke, I am your Father!',
    ]

    if 'Luke' in message.content:
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == 'Andy':
        with open('andy.gif', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
            # picture = discord.File(f)
            # await message.channel.send(file=picture)

client.run(TOKEN)
