from discord.ext import commands
from discord.ext import tasks
#from datetime import datetime
import os
import traceback
cnt = 0
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def map(ctx):
    await ctx.send('地図を持って来てやったぞ！\nhttps://webstatic-sea.mihoyo.com/app/ys-map-sea/index.html?lang=ja-jp#/map/2?lang=ja-jp&shown_types=3,132,133,134,135,136,137,138,157,2,154,181&center=1002.58,-589.05&zoom=-2.50')

@bot.command()
async def test(ctx):
    cnt + 1
#    if cnt<3:
    await ctx.send('オイラだぞ！ちゃんと届いてるよな？')
"""
    else
        cnt = 0
        await ctx.send('……おい！オイラで遊んでるだろ！！')
"""
bot.run(token)
