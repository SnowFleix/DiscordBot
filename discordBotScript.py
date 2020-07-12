import discord

bannedWords = {"puta", "porca", "burra", "burro", "estupida", "estupido", "merda", "caralho", "cona", "pila"}


class PortugalClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if any(word in message.content for word in bannedWords):
            await message.channel.send("Add text here")
    async def on_message_delete(self, message):
        #if message.author.name == "": # add this if you want only one person to have their deleted messages reposted
        await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))


client = PortugalClient()
client.run("Your token goes here")