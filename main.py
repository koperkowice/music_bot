# github.com/koperkowice/music_bot.git
# dont copy

import discord
from discord.ext import commands
import youtube_dl
import json

with open('token.json') as tkkk:
  data=json.load(tkkk)
  token=data[0]['token']

bot = commands.Bot(command_prefix='\')

@bot.event
async def on_ready():
  print('repo: github.com/koperkowice/music_bot.git')
  print('ready')

@bot.command()
async def j(ctx):
    if ctx.author.voice is None:
        await ctx.send(":no_entry_sign: - You aren't in voice channel!")
    
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
        await ctx.send(":white_check_mark: - Joined To Voice Channel!")
    else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
        await ctx.send(":white_check_mark: - Joined To Voice Channel!")

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send(":no_entry_sign: - You aren't in voice channel!")
    
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
        await ctx.send(":white_check_mark: - Joined To Voice Channel!")
    else:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
        await ctx.send(":white_check_mark: - Joined To Voice Channel!")

@bot.command()
async def d(ctx):
    await ctx.send(":white_check_mark: - Disconnected!")
    await ctx.voice_client.disconnect()

@bot.command()
async def disconnect(ctx):
    await ctx.send(":white_check_mark: - Disconnected!")
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx,url):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info=ydl.extract_info(url, download=False)
        url2=info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)

@bot.command()
async def p(ctx,url):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info=ydl.extract_info(url, download=False)
        url2=info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)

@bot.command()
async def pause(ctx):
    await ctx.voice_client.pause()
    await ctx.send(":white_check_mark: - Paused!")

@bot.command()
async def resume(ctx):
    await ctx.voice_client.resume()
    await ctx.send(":white_check_mark: - Resumed!")

bot.run(token)
