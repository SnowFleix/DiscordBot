import discord

class PortugalClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if "foda se" in message.content.lower():
            await message.channel.send("I'd rather not tbh")
        elif message.content.lower() == "caralho":
            await message.channel.send("Yes I have big")
        elif message.content.lower() == "po caralho bot de merda":
            await message.channel.send("No u")
        elif "estupida bot" in message.content.lower():
            await message.channel.send("I'm sorry I hurt your feelings when I called you stupid, I just thought you already knew")
    async def on_message_delete(self, message):
        if message.author.name == "|Inês| (ijwtbhfe)":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))
        if message.author.name == "fleix":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.name, message.content))


client = PortugalClient()
client.run("")
