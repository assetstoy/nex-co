import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1261927093940518915)  # YOUR_CHANNEL_ID에는 메시지를 보낼 채널의 ID를 넣어주세요
    if channel:
        await channel.send('{member.name}님, NEX STUDIO에 오신 것을 환영합니다! 인증 후 이용약관에 동의해주세요!')

bot.run('1261950439549829203')
