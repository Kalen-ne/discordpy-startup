import discord

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client.event = discord.Client()

@client.event
async def pn_rady():
    print('ログインしました')

@client.event 
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/Oppai'
        await message.channel.send('おっぱい')

client.run(token)
