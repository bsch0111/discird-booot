import discord
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
app_token = config['DEFAULT']['SLASH_APP_TOKEN']
print(app_token)
client = discord.Client()

@client.event
async def on_ready():
    print(f'방금 로그인 하셨습니다. {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        print("message 담당자와 클라이언트 담당자가 일치합니다.")
        return

    if message.content.startswith("$hello"):
        await message.channel.send(message.author)
        await message.channel.send(client.user)
        await message.channel.send("id :" + str(client.user.id))
        await message.channel.send("hello")
        await message.channel.send("hello2")
    if message.content.startswith("$profile"):
        profile = await message.author.profile()
        print(profile)
        

    await message.reply('Reply', mention_author=True)

client.run(app_token)

# logger = loggin.getlogger('discord')
# logger.setLevel(loggin.DEBUG)
# handler = loggin.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
# logger.addHandler(handler)