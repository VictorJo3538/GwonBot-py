from nextcord.ext import commands
import nextcord
import random
import os
from webdriver import keep_alive

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

Gwon_Channel = 1043962135744610445

@bot.listen("on_ready")
async def on_ready():
    print(f'{bot.user.name} 작동완료')
    await bot.change_presence(status=nextcord.Status.online,
                              activity=nextcord.Game("리듬게임 생각"))


@bot.listen('on_message')
async def on_message(msg):
    # 사용자 ID
    GYH = 1045304676217798658
    JYW = 355676639801114627
    LYJ = 366832595906068490
    JSM = 340336549411422229
    GBG = 1044331314616205403
    LDH = 322025515344986122
    KDG = 1045198399231754301
    ch = bot.get_channel(Gwon_Channel)
    # 권영훈 대답 리스트
    main_message = [
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045306360448958534/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045305532329771018/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045305551950729276/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045305762009849906/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045615262386372638/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045839910399127612/image0.jpg',
        'https://cdn.discordapp.com/attachments/1043962135744610445/1045840083388997772/image0.jpg',
        '깝 ㄴㄴ', 'ㅤ', '👺', 'ㅋㅋ', '너 뭐야', '너 누구야', '그래', '싫음', '왜', '흠....',
        '흠집', '우어', '우어', '이거 진짜 흠인데', '난 그럴수 있다 생각해', '아싸', '헉!', '와..',
        '얼탱이 없네 🤣', "I'm scared", '나는 두려워', '나이스', 'yee', '킄킄', '어쩔맨', '와이'
    ]
    GYH_message = ['모야 이 짭은', '권영훈 안물']
    JYW_message = [
        '전영우 안물', '전 짱', '전영우 짱바보', '어이 전', '전.....', '저전......', '어이 전씨'
    ]
    LYJ_message = ['이유진 짱', '이유진 뭐라는거지?', '이유진 안물', '이유진 짱바보', '이유진진자라']
    JSM_message = ['조승민 안물', '어이 조씨']
    GBG_message = ['금보경 안물', '어이 금씨']
    LDH_message = ['임도현 안믈', '임도현 짱']
    KDG_message = ['강동근 안물', '강동근 전문하사 하자']

    P_list = [GYH, JYW, LYJ, JSM, GBG, LDH, KDG]
    P_Dic = {
        GYH: GYH_message,
        JYW: JYW_message,
        LYJ: LYJ_message,
        JSM: JSM_message,
        GBG: GBG_message,
        LDH: LDH_message,
        KDG: KDG_message
    }

    # 권영훈수두기
    if msg.channel.id == 1043962135744610445 and '권영훈수두기' in msg.content:
        if msg.author.id == LDH:
            P_Dic[LDH].append('임도현자타임')
            await ch.send(random.choice(P_Dic[LDH]))
            P_Dic[LDH].remove('임도현자타임')
            return

    # 권영훈 대답 매크로
    if msg.channel.id == 1043962135744610445 and ('어이 권' in msg.content
                                                  or '영훈' in msg.content):
        for P in P_list:
            if msg.author.id == P:
                await ch.send(random.choice(P_Dic[P] + main_message))
                return
        await ch.send(random.choice(main_message))

    # 전영우 저전 매크로
    if msg.author == bot.user:
        return

    if msg.author.id == 355676639801114627 and '전' in msg.content:
        await msg.channel.send('전영우짱바보')
        return

    if msg.content == '전':
        await msg.channel.send('저전')

    if msg.content.endswith('저전'):
        await msg.channel.send('저' + msg.content)
    # 봇이 대답한것 생략
    if msg.author == bot.user:
        return

def start():
    bot.run(os.environ['TOKEN'])


start()
