import discord
import TOKEN
import time

TOKEN = TOKEN.TOKEN

client = discord.Client()

# sleep time
st=0.7

# voice
music = 'nice.mp3'
source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music), volume=0.5)

@client.event
async def on_ready():
    print('起動しました')


@client.event
async def on_message(message):
    vc = message.guild.voice_client
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


    # 絵文字を直接書き込む
    if message.content == '👍' or message.content == '👍🏻' or message.content == '👍🏼' or message.content == '👍🏽' or message.content == '👍🏾' or message.content == '👍🏿' or message.content == 'b' or message.content == 'nice' or message.content == 'ナイス' or message.content == 'ないす' or message.content == 'ナイスな椅子' or message.content == '優' or message.content == '良' or message.content == '可' or message.content == 'Nice' or message.content == 'd' or message.content == '6':
        if message.author.voice is None:
            print('ボイスチャンネルに接続していません')
            return
        print('Nice')


        # 音声を再生
        try:
            time.sleep(st)
            message.guild.voice_client.stop()
        except:
            pass
        finally:
            print("Err")
        message.guild.voice_client.play(source)

    if message.content == '!nice.help':
        await message.channel.send('This bot was created by Wurzeit...Nice...version2.2\n\n\
----------List of Functions----------\n\
・!nice   bot joins the call\n\
・!bad   bot leaves the call\n\
・👍 , nice, ナイス, ないす, b.....Nice')
        print('send nice.help')

    if message.content == 'いいね' or message.content == 'いいですね' or message.content == 'よき' or message.content == 'よきですね':
        await message.channel.send('Nice...')

    if message.content == '!nice.volume':
        await message.channel.send('The default volume is nice and big...')

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

        # 音声を再生
        try:
            time.sleep(st)
            reaction.message.guild.voice_client.stop()
        except:
            pass
        finally:
            print("Err")
        reaction.message.guild.voice_client.play(source)


client.run(TOKEN)
