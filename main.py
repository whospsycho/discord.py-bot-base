import discord
import os

cwd = os.path.dirname(os.path.realpath(__file__))

with open(cwd + '\config.json') as f:
    config = json.load(f)


token = config.get('token')
prefix = config.get('prefix')



client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('Bot online!')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')







client.run(token)