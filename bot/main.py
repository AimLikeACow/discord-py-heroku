import discord

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("NzQ3ODkzMjM3MjUwNzg1MzEx.X0Vf2g.kTRKzK6XfFf_g6HTqPoWLMvWon8")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

client.run(TOKEN)
