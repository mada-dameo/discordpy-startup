import os
import discord
import datetime
import pytz
from discord.ext import tasks
from asyncio import sleep


TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%H:%M')
    channel = client.get_channel(CHANNEL_ID)
    print(now)
    print(channel)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
if TOKEN is None or CHANNEL_ID is None:
    print('環境変数が適切に設定されていません')
else:
    client.run(TOKEN)
