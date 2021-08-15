import discord
from urllib import request
import logging

client = discord.Client()
CategoryID = 876410471115272253


@client.event
async def on_ready():       #bot has logged in and has set things up 
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:

        if(message.content.startswith('!send')):

            messageContent = message.content
        
            for channel in message.guild.text_channels:
                print('Sending something!')
                print(messageContent)
                if(channel.category.id == CategoryID):
                    await channel.send(messageContent)

        

client.run('ODc2MzM2NjUyOTEyNTcwMzY5.YRimGw.tscmdX65C9t0jnpKdtGGe1tqT6Y')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)