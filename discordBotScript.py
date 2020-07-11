import _thread
import discord
from discord.utils import get


def time_user_out(message):
    role = get(message.author.roles, name="Timeout")
    client.add_role(message.author, role)


class PortugalClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author.name == "fleix" and "puta" in message.content:
            _thread.start_new(time_user_out(message), ())
        if message.author.name == "|Inês| (ijwtbhfe)" and "puta" in message.content:
            await message.channel.send("Sim puta, veeerrrryyyy smart")
        #print(message)
    async def on_message_delete(self, message):
        if message.author.name == "|Inês| (ijwtbhfe)":
            await message.channel.send('{0} tried to delete: {1}'.format(message.author.nick, message.content))


client = PortugalClient()
