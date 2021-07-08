from discord.ext import commands
from discord.ext import tasks
#from datetime import datetime
import datetime
import os
import traceback
bot = commands.Bot(command_prefix="/")
token = os.environ["DISCORD_BOT_TOKEN"]
ch = os.environ["CHANNEL_ID"]
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



	await bot.process_commands(message)

##########################################     コマンド     ###################################################


@bot.command()
async def map(ctx):
	await ctx.send("地図を持って来てやったぞ！\nhttps://webstatic-sea.mihoyo.com/app/ys-map-sea/index.html?lang=ja-jp#/map/2?lang=ja-jp&shown_types=3,132,133,134,135,136,137,138,157,2,154,181&center=1002.58,-589.05&zoom=-2.50")
@bot.command()
async def code(ctx):
	await ctx.send("ここにはお宝が隠されてるらしいぞ、早く探そうぜ！\nhttps://genshin.mihoyo.com/m/ja/gift")
@bot.command()
async def test(ctx):
    global callcnt
    callcnt += 1
    if callcnt<=3:
        await ctx.send("オイラだぞ！ちゃんと届いてるよな？")
        #await ctx.send(callcnt)
    elif callcnt>=4:
        await ctx.send("おい！！オイラで遊んでるだろ！")
        callcnt = 0
        #await ctx.send(callcnt)
@bot.command()
async def paimon(ctx):
	await ctx.send("```\n/map\n/code\n/test\n```")

@bot.command()
async def time(ctx):
	now = datetime.datetime.now().strftime('%H:%M')
	await ctx.send(now)


##########################################     コマンドエラー     ###################################################


@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = "".join(traceback.TracebackException.from_exception(orig_error).format())
	await ctx.send(error_msg)


##########################################     タスク     ###################################################

@tasks.loop(seconds=60)
async def loop():
	now = datetime.datetime.now().strftime('%H:%M')
	#channel = bot.get_channel["CHANNEL_ID"]
	#channel = bot.get_channel["CHANNEL_ID"]
	#if now == '22:41':
	channel = bot.get_channel(ch)
	await channel.send("loopが回ったぞ")
loop.start()

bot.run(token)
