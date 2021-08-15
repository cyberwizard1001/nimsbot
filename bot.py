import discord
import logging
import asyncio

client = discord.Client()
CategoryID = 876410471115272253


@client.event
async def on_ready():  # bot has logged in and has set things up
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!send"):

        attachments = [attachment.url for attachment in message.attachments]

        tasks = [
            asyncio.create_task(channel.send(f"{message.content} {' '.join(attachments)}"))
            for channel in message.guild.text_channels
            if channel.category.id == CategoryID
        ]

        for task in tasks:
            await task


client.run("ODc2MzM2NjUyOTEyNTcwMzY5.YRimGw.tscmdX65C9t0jnpKdtGGe1tqT6Y")

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)
