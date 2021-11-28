import discord
import TOKEN

TOKEN = TOKEN.TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('起動しました')


@client.event
async def on_message(message):
    vc = message.guild.voice_client
    music = 'nice.mp3'
    if message.author.bot:
        return
    if message.content == '!nice':
        if message.author.voice is None:
            print('ボイスチャンネルに接続していません')
            return
        await message.author.voice.channel.connect()
        print('通話に接続しました')


    elif message.content == '!bad':
        if vc is None:
            print('ボイスチャンネルに接続していません')
            return
        await vc.disconnect()
        print('通話から切断しました')

    if message.content == '👍' or message.content == '👍🏻' or message.content == '👍🏼' or message.content == '👍🏽' or message.content == '👍🏾' or message.content == '👍🏿':
        if message.author.voice is None:
            print('ボイスチャンネルに接続していません')
            return
        print('Nice')
        message.guild.voice_client.play(discord.FFmpegPCMAudio(music))

    if message.content == '!nice.help':
        await message.channel.send('This bot was created by Wurzeit...Nice\n\n\
                                   ----------List of Functions----------\n\
                                   ・!nice   bot joins the call\n\
                                   ・!bad   bot leaves the call\n\
                                   ・👍   Nice')

@client.event
async def on_reaction_add(reaction, user):
    vc = reaction.message.guild.voice_client
    music = 'nice.mp3'
    print(f"{user}さんの付けたリアクションを検出しました")
    if reaction.emoji == '👍' or reaction.emoji == '👍' or reaction.emoji == '👍🏻' or reaction.emoji == '👍🏼' or reaction.emoji == '👍🏽' or reaction.emoji == '👍🏾' or reaction.emoji == '👍🏿':
        if reaction.message.author.voice is None:
            print('ボイスチャンネルに接続していません')
            return
        print('Nice')
        reaction.message.guild.voice_client.play(discord.FFmpegPCMAudio(music))


client.run(TOKEN)
