import discord
import random

yoMamaJokes = ["Yo momma is so fat when she got on the scale it said, \"I need your weight not your phone number.\"",
               "Yo momma is so fat, I took a picture of her last Christmas and it's still printing.",
               "Yo momma is so fat that when she went to the beach a whale swam up and sang, \"We are family, even though you're fatter than me.\"",
               "Yo mamma is so ugly when she tried to join an ugly contest they said, \"Sorry, no professionals.\"",
               "Yo momma's so fat and old when God said, \"Let there be light,\" he asked your mother to move out of the way.",
               "Yo momma's so fat, that when she fell, no one was laughing but the ground was cracking up.",
               "Yo momma is so fat when she sat on WalMart, she lowered the prices.",
               "Yo momma is so fat that Dora can't even explore her!",
               "Yo momma is so stupid when an intruder broke into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldn't find the \"CALL\" button.",
               "Your momma is so ugly she made One Direction go another direction.",
               "Yo momma is so fat her bellybutton gets home 15 minutes before she does.",
               "Yo momma's so stupid, she put two quarters in her ears and thought she was listening to 50 Cent.",
               "Yo momma so stupid she stuck a battery up her ass and said, \"I GOT THE POWER!\"",
               "Yo momma's so dumb, when y'all were driving to Disneyland, she saw a sign that said \"Disneyland left,\" so she went home.",
               "Yo momma is so hairy, when she went to the movie theater to see Star Wars, everybody screamed and said, \"IT'S CHEWBACCA!\"",
               "Yo momma is so stupid she climbed over a glass wall to see what was on the other side.",
               "Yo mamma is so fat she doesn't need the internet, because she's already world wide.",
               "Yo momma is so stupid she brought a spoon to the super bowl.",
               "Yo Momma's so fat when I told her to touch her toes she said, \"What are those\"?",
               "Yo momma is so fat, when she sat on an iPod, she made the iPad!",
               "Yo momma is so stupid she took a ruler to bed to see how long she slept.",
               "Yo momma's so fat she needs cheat codes for Wii Fit.",
               "Yo mamma is so ugly when she took a bath the water jumped out.",
               "Yo momma's so fat, that when she went to the zoo, the hippos got jealous."]


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
        elif "tell me a yo mama joke" in message.content.lower():
            await message.channel.send(random.choice(yoMamaJokes))
    async def on_message_delete(self, message):
        if message.author.name == "|Inês| (ijwtbhfe)":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))
        if message.author.name == "fleix":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.name, message.content))


client = PortugalClient()
client.run("")
