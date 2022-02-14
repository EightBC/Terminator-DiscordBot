# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content.startswith('$'):
        if isinstance(message.author, discord.Member) and not len(message.author.roles) == 1:
            pass
        else:
            counter = 0
            for channel in message.guild.text_channels:
                async for msg in channel.history(limit=10):
                    if msg.content == message.content:
                        counter += 1
            if counter > 4:
                bomj = message.author
                await ban_function(bomj, message)
                return


    # if message.content.startswith('$ban'):
    #     bomj = message.mentions[0]
    #     await ban_function(bomj, message)
    #     return

    if message.content.startswith('$owner'):
        await message.channel.send(type(message.guild.owner))

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


async def ban_function(bomj, message):
    try:
        await message.guild.fetch_ban(bomj)
    except discord.errors.NotFound:
        if bomj.dm_channel == None:
            await bomj.create_dm()
        await bomj.dm_channel.send('Тааа\nШааа\nПиши 8bc#5255 если хочешь вернуться в уличные гонки')
        await message.channel.send(f'Member {bomj} has been banned. Reason: Spam')
        await message.guild.ban(bomj, reason="лох", delete_message_days=1)


f = open('token.txt', 'r')
t = f.readline().strip()
f.close()

client.run(t)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
