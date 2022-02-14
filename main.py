# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import discord

client = discord.Client()

spam_channels = [
    942402858408636499 #клипы
]
SPAM_LIMIT = 3
HISTORY_LIMIT = 10


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_guild_channel_create(channel):
    await channel.send('This channel now not in spam mode')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in spam_channels:
        return

    if not message.content.startswith('!'):
        if isinstance(message.author, discord.Member) and len(message.author.roles) <= 1:
            counter = 0
            for channel in message.guild.text_channels:
                if channel.id not in spam_channels:
                    async for msg in channel.history(limit=HISTORY_LIMIT):
                        if msg.content == message.content and msg.author.id == message.author.id:
                            counter += 1
            if counter > SPAM_LIMIT:
                bomj = message.author
                await ban_function(bomj, message)
                return


    if message.content.startswith('$add spam channel'):
        pass



@client.event
async def on_message_edit(before, after):
    pass

async def ban_function(bomj, message):
    if bomj.id == bomj.guild.owner_id:
        await message.channel.send(f'Member {bomj} has *not* been banned. Reason: God')
        return

    try:
        await message.guild.fetch_ban(bomj)
    except discord.errors.NotFound:
        if bomj.dm_channel == None:
            await bomj.create_dm()
        await bomj.dm_channel.send('Тааа\nШааа\nПиши 8bc#5255 если хочешь вернуться в уличные гонки')
        await message.guild.ban(bomj, reason="лох", delete_message_days=1)
        await message.channel.send(f'Member {bomj} has been banned. Reason: Spam')




f = open('token.txt', 'r')
t = f.readline().strip()
f.close()

client.run(t)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
