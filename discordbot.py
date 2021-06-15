from discord.ext import commands
from discord.ext import tasks
#from datetime import datetime
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
#channel = discord.utils.get(guild.text_channels, name="テイワット")
callcnt = 0




##########################################     会話     ###################################################


@bot.event
async def on_message(message):
	"""メッセージを処理"""
	if message.author.bot:  # ボットのメッセージをハネる
		return
	
	if message.content == "えへっ。":
		await message.channel.send("「えへっ」ってなんだよ…！！")
	if message.content == "おはよう":
		await message.channel.send("おはよう旅人！今日も良い朝だな！！")



##########################################     コマンドエラー     ###################################################


@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	await ctx.send(error_msg)


##########################################     コマンド     ###################################################


@bot.command()
async def map(ctx):
	await ctx.send('地図wo持って来てやったぞ！\nhttps://webstatic-sea.mihoyo.com/app/ys-map-sea/index.html?lang=ja-jp#/map/2?lang=ja-jp&shown_types=3,132,133,134,135,136,137,138,157,2,154,181&center=1002.58,-589.05&zoom=-2.50')
	



"""
@bot.command()
async def map(ctx):
	await ctx.send('地図wo持って来てやったぞ！\nhttps://webstatic-sea.mihoyo.com/app/ys-map-sea/index.html?lang=ja-jp#/map/2?lang=ja-jp&shown_types=3,132,133,134,135,136,137,138,157,2,154,181&center=1002.58,-589.05&zoom=-2.50')

	


@bot.command()
async def code(ctx):
    await ctx.send('ここにはお宝が隠されてるらしいぞ、早く探そうぜ！\nhttps://genshin.mihoyo.com/m/ja/gift')

@bot.command()
async def test(ctx):
    global callcnt
    callcnt += 1
    if callcnt<=3:
        await ctx.send('オイラだぞ！ちゃんと届いてるよな？')
        #await ctx.send(callcnt)
    elif callcnt>=4:
        await ctx.send('おい！！オイラで遊んでるだろ！')
        callcnt = 0
        #await ctx.send(callcnt)

@bot.command()
async def phelp(ctx):
    await ctx.send('```\n/map\n/code\n/test\n```')

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    print(now)
    if now == '20:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone \n今日のWebログインは受け取ったか？\nURLを貼っておいてやるから感謝しろよな！\nhttps://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481\n')  

"""
bot.run(token)
