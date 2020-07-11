import discord

bannedWords = {"puta", "porca", "burra", "burro", "estupida", "estupido"}


class PortugalClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if any(word in message.content for word in bannedWords):
            await message.channel.send("Don't make me simp you, if you say that shit again imma simp you bad")
    async def on_message_delete(self, message):
        if message.author.name == "|Inês| (ijwtbhfe)":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))
        if message.author.name == "fleix":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))


client = PortugalClient()
