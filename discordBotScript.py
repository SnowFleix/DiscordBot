import discord
import random

bannedWords = {"puta", "porca", "burra", "burro", "estupida", "estupido", "merda", "caralho", "cona", "pila"}
rudeWordResponses = ["Could you say that again with grown-up language?",
                     "Your use of such derogatory language simply shows that your ability to articulate does not extend beyond the word 'f*ck'.",
                     "I would insult you back, but I’m afraid it might be incomprehensible to you.",
                     "Do you kiss your mother with that mouth?",
                     "You were raised like a wild animal",
                     "Your cursing is only showing your lack of intelligence and inability to express yourself with words",
                     "Why does offending people with your diarrhea of the mouth make you think you are gaining approval and acceptance?",
                     "Maybe you can try say somethingggggg smart?"]


class PortugalClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if any(word in message.content for word in bannedWords):
            await message.channel.send(random.choice(rudeWordResponses))
        if "lets fuck" in message.content:
            await message.channel.send("I'd rather not tbh")
        if "Foda se" in message.content:
            await message.channel.send("I'd rather not tbh")
        if message.content == "caralho":
            await message.channel.send("I don't think anyone wants to with you tbh")
    async def on_message_delete(self, message):
        if message.author.name == "|Inês| (ijwtbhfe)":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))
        if message.author.name == "fleix":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))


client = PortugalClient()
client.run("")