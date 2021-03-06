import discord
import logging
import asyncio
import keep_alive

client = discord.Client()
CategoryID = 877541025328021584
keep_alive.keep_alive()

@client.event
async def on_ready():  # bot has logged in and has set things up
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:

        if message.content.startswith("!send"):

            messageContent = message.content

            action = messageContent[5:]

            tasks = []

            for channel in message.guild.text_channels:
                print("Sending something!")
                print(messageContent)
                if channel.category.id == CategoryID:
                    tasks.append(asyncio.create_task(channel.send(action)))

            for task in tasks:
                await task


client.run("ODc2MzM2NjUyOTEyNTcwMzY5.YRimGw.tscmdX65C9t0jnpKdtGGe1tqT6Y")

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

