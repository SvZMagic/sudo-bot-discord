import nextcord
from nextcord.ext import commands, tasks
from nextcord import Interaction
from nextcord.abc import GuildChannel
import nextcord.utils
from nextcord.ext.commands import cooldown, BucketType
from nextcord.errors import Forbidden
from nextcord.ui import Button, View, Modal, TextInput
from nextcord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, MissingPermissions, CommandOnCooldown)
import pyshorteners
import asyncio, datetime, os, io, contextlib
import random
import urllib
import json
import sqlite3
from requests import get
import aiohttp
#from wavelink.ext import spotify
import wavelink
import aiosqlite
from io import BytesIO
import psutil
#from easy_pil import *
import datetime
import time
from nextcord import Interaction, SlashOption, ChannelType
import humanfriendly
from nextcord.ext import application_checks
from asyncio import sleep 
from itertools import cycle
import string
from nextcord.utils import format_dt
import difflib
from difflib import get_close_matches
from contextlib import suppress
import traceback
import requests

#urlgpt = "https://you-chat-gpt.p.rapidapi.com/"


PREFIX = '$sudob '
print("Zetabyte. 2023")

imgscats = ['https://i.postimg.cc/bvCT7tzC/Screenshot-20220629-173035.jpg',
            'https://i.postimg.cc/28S56LmF/photo-2022-06-28-21-50-18.jpg', 
            'https://i.postimg.cc/W3SvLSDR/photo-2022-06-30-23-56-14.jpg',
            'https://i.postimg.cc/N0tYP4Yt/IMG-f89a0f657343f2015c3ece7a23e78b57-V.jpg',
            'https://i.postimg.cc/bvjPkKmk/1561011173-8-1.jpg',
            'https://i.postimg.cc/pLb46KKt/786fc0798233006257d41dc0132f6387-1.jpg']

imgdogs = ['https://i.postimg.cc/Bnm6RHsb/shutterstock-231364474-2.jpg', 'https://i.postimg.cc/TwD3ysb5/0e26b1b65946ee36fac9605ae67e4ac8.jpg', 'https://i.postimg.cc/zXjXRKy7/d381cb1cdcf05cbc6dce920f76ee7555.jpg', 'https://i.postimg.cc/MppZ0HRS/1936556.jpg']

sudobot = commands.Bot(command_prefix = "$sudob ", strip_after_prefix = True, intents=nextcord.Intents.all())
sudobot.persistent_views_added = False
sudobot.remove_command("help")

rcats = requests.get('https://some-random-api.ml/animal/cat')
#print(rcats.json()["image"]) 
apicats = rcats.json()["image"]
custumcats = random.choice(imgscats)

async def change_status():
    statuses = cycle(
        [
            "$sudo help",
            "Версия 0.6.6 M2",
            f"На {len(sudobot.guilds)} серверах!"
        ]
    )

    while not sudobot.is_closed():
        await sudobot.change_presence(activity=nextcord.Game(name=next(statuses)))
        await asyncio.sleep(5)

@sudobot.event
async def on_ready():
    print('Бот запущен')
#    change_status()
    sudobot.loop.create_task(change_status())


@sudobot.event
async def on_command_error(ctx, exc):
  if isinstance(exc, BadArgument):
    await ctx.reply(embed=nextcord.Embed(
 	    title=f"<:no:997034584728416307> Неправильные аргументы!",
 	    description="Найдены неправильные аргументы!",
 	    color=nextcord.Colour.red()
 	  ))
  elif isinstance(exc, commands.CommandNotFound):
    cmd = ctx.invoked_with
    cmds = [cmd.name for cmd in sudobot.commands]
    matches = get_close_matches(cmd, cmds)
    if len(matches) > 0:
      await ctx.send(embed = nextcord.Embed(
        title=f"<:no:997034584728416307>  Команда не найдена!",
        description=f"Команда `$sudo {cmd}` не найдена, может быть вы имелли ввиду `$sudo {matches[0]}`?",
        color=nextcord.Colour.red()
      ))
    else:
      return await ctx.send(embed = nextcord.Embed(
        title=f"<:no:997034584728416307>  Команда не найдена!",
        description=f"Пожалуйста напишите  `$sudo help` чтобы увидеть список команд!",
        color=nextcord.Colour.red()
      ))
  elif isinstance(exc, commands.CommandOnCooldown):
    await ctx.send(embed = nextcord.Embed(title = ":hourglass:  Команда перезаряжается!", description = f"Команда перезаряжается, повторите попытку {round(exc.retry_after, 2)} секунды.", color=nextcord.Colour.red()), ) 
  elif isinstance(exc, commands.MissingPermissions):
    await ctx.reply(embed=nextcord.Embed(
 	    title=f"<:no:997034584728416307>  Не хватает прав!",
 	    description=f"Вам нужны  `{', '.join([err.lower().replace('_', ' ') for err in exc.missing_permissions])}` чтобы вы могли использовать команду!",
 	    color=nextcord.Colour.red()
 	  ))
  elif isinstance(exc, commands.MissingRequiredArgument):
    await ctx.reply(embed=nextcord.Embed(
 	    title=f"<:no:997034584728416307>  Не хватает аргумента!",
 	    description=f"Не хватает аргумента: `{exc.param.name}`",
 	    color=nextcord.Colour.red()
 	  ))
  else:
 	  traceback.print_exception(type(exc), exc, exc.__traceback__)

@sudobot.event
async def on_message(message):
  guild = message.guild
  author = message.author
  if message.content == "<@942005986921685073>":
    return await message.channel.send("Привет! Я $sudo-bot. Мой префикс - `$sudo ` и `/`")
  await sudobot.process_commands(message)
 
@sudobot.command()
async def clear(ctx, amount: int=100):
    await ctx.send(embed = nextcord.Embed(
    description="Извините, но данная функция работает только через `/`.",
		color = 0x2F3136
	))

@sudobot.command()
async def help(ctx):
   emb = nextcord.Embed(title = 'Навигация по командам:')

   emb.add_field( name = '{}hack'.format(PREFIX), value = 'взламывает пользователя (не по-настоящему)', inline = False)
   emb.add_field( name = '{}invite'.format(PREFIX), value = 'выдает ссылку на бота', inline = False)
   emb.add_field( name = '{}ver'.format(PREFIX), value = 'показывает версию', inline = False)
   emb.add_field( name = '{}cat'.format(PREFIX), value = 'показывает картинку с котом', inline = False)
   emb.add_field( name = '{}dog'.format(PREFIX), value = 'показывает картинку с собакой', inline = False)
   emb.add_field( name = '{}ban [пользователь]'.format(PREFIX), value = 'банит пользователя', inline = False)
   emb.add_field( name = '{}kick [пользователь]'.format(PREFIX), value = 'кикает пользователя', inline = False)
   emb.add_field( name = '{}unban [пользователь]'.format(PREFIX), value = 'разбанит пользователя', inline = False)
   emb.add_field( name = '{}clear [количество]'.format(PREFIX), value = 'чистит чат', inline = False)
   emb.add_field( name = '{}ball [вопрос]'.format(PREFIX), value = 'отвечает на вопрос', inline = False)
   await ctx.send( embed = emb )

@sudobot.slash_command(name = "help", description="Показывает команды")
async def hlp(interaction: Interaction):
   emb = nextcord.Embed(title = 'Навигация по командам:')

   emb.add_field( name = '{}hack'.format(PREFIX), value = 'взламывает пользователя (не по-настоящему)', inline = False)
   emb.add_field( name = '{}invite'.format(PREFIX), value = 'выдает ссылку на бота', inline = False)
   emb.add_field( name = '{}ver'.format(PREFIX), value = 'показывает версию', inline = False)
   emb.add_field( name = '{}cat'.format(PREFIX), value = 'показывает картинку с котом', inline = False)
   emb.add_field( name = '{}dog'.format(PREFIX), value = 'показывает картинку с собакой', inline = False)
   emb.add_field( name = '{}ban [пользователь]'.format(PREFIX), value = 'банит пользователя', inline = False)
   emb.add_field( name = '{}kick [пользователь]'.format(PREFIX), value = 'кикает пользователя', inline = False)
   emb.add_field( name = '{}unban [пользователь]'.format(PREFIX), value = 'разбанит пользователя', inline = False)
   emb.add_field( name = '{}clear [количество]'.format(PREFIX), value = 'чистит чат', inline = False)
   emb.add_field( name = '{}ball [вопрос]'.format(PREFIX), value = 'отвечает на вопрос', inline = False)
   await interaction.send( embed = emb )
 
@sudobot.command()
async def cat(ctx):
    cats = [
        f"{apicats}",
        f"{custumcats}"
        ]
    await ctx.send(random.choice(cats))

@sudobot.slash_command(name = "cat", description="Показывает картинку с котом")
async def pngcat(interaction: Interaction):
    await interaction.send(random.choice(imgscats))

@sudobot.command()
async def killbot(ctx):
    if ctx.author.id == 922190067227828285:
        await ctx.reply(embed = nextcord.Embed(
            title = 'Пожалуйста подождите!',
            description = "Бот выключится через 3 секунды!",
            color = 0x2F3136 ))
        await asyncio.sleep(3)
        await sudobot.close()
    else:
        await ctx.send(embed = nextcord.Embed(title = '<:no:997034584728416307>   Ошибка',
          description ="Команда доступна ТОЛЬКО разработчикам!",color = 0x2F3136))

@sudobot.command()
async def heck(ctx, *, member):
     hacksye = [
		" был успешно взломан!",
                " не был взломан. И даже не пытайтесь больше, всё равно не выйдет даже в интернет",
                f" был взломан. Теперь {member} стал иллюминатом",
                " не был успешно взломан"
                " вообще не взломан. ГДЕ ИНТЕРНЕТ????"
			]
     await ctx.send(embed = nextcord.Embed(
                description=f"{member} {random.choice(hacksye)}",
		color = 0x2F3136
	))

@sudobot.slash_command(name = "heck", description="Взламывает пользователя (не по-настоящему)")
async def hack(interaction: Interaction, *, member):
    hacksye = [
		"был успешно взломан!",
                "не был взломан. И даже не пытайтесь больше, всё равно не выйдет даже в интернет",
                f"был взломан. Теперь {member} стал иллюминатом",
                "не был успешно взломан"
                "вообще не взломан. ГДЕ ИНТЕРНЕТ????"
			]
    await interaction.send(embed = nextcord.Embed(
                description=f"{member} {random.choice(hacksye)}",
		color = 0x2F3136
	))

@sudobot.command()
async def ver(ctx):
     await ctx.send(embed = nextcord.Embed(
                description="Версия 0.6.6 M2",
		color = 0x2F3136
	))

@sudobot.command()
async def secretGPT(ctx, *, question):
     payload = {
	"question": f"{question}",
	"max_response_time": 30
     }
     headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": "2efd2d7517mshdb43f0240596168p1c8568jsna108c04c5af6",
    	"X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
     }
     response = requests.request("POST", urlgpt, json=payload, headers=headers)
     
     await ctx.send(embed = nextcord.Embed(
         title = f'Вопрос: {question}',
         description="```" + response.text + "```",
		color = 0x2F3136
	))

@sudobot.slash_command(name = "ver", description="Показывает версию")
async def sudover(interaction: Interaction):
     await interaction.send(embed = nextcord.Embed(
                description="Версия 0.6.6 M1",
		color = 0x2F3136
	))

@sudobot.command()
async def ball(ctx, *, question):
  answers = [
		"Да",
		"Может быть",
		"Конечно",
		"Не знаю",
		"Уж точно **нет**",
		"Нет",
		"Я думаю, нет"
			]
  await ctx.send(embed=nextcord.Embed(
		title="Ответ:",
		description=f"Вопрос: {question} \n\n Ответ: {random.choice(answers)}",
		color = 0x2F3136
	))

@sudobot.slash_command(name = "ball", description="Отвечает на вопрос")
async def ball(interaction: Interaction, *, question):
  answers = [
		"Да",
		"Может быть",
		"Конечно",
		"Не знаю",
		"Уж точно **нет**",
		"Нет",
		"Я думаю, нет"
  ]
  await interaction.send(embed=nextcord.Embed(
		title="Ответ:",
		description=f"Вопрос: {question} \n\n Ответ: {random.choice(answers)}",
		color = 0x2F3136
	))

@sudobot.command()
async def invite(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=942005986921685073&permissions=274879028294&scope=bot')

@sudobot.slash_command(name = "invite", description="Дает ссылку на бота")
async def invitebot(interaction: Interaction):
    await interaction.send('https://discord.com/oauth2/authorize?client_id=942005986921685073&permissions=274879028294&scope=bot')

@sudobot.command()
async def dog(ctx):
    await ctx.send(random.choice(imgdogs))

@sudobot.slash_command(name = "dog", description="Показывает картинку с собакой")
async def pngdog(interaction: Interaction):
    await interaction.send(random.choice(imgdogs))

@sudobot.command()
@commands.has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, member: nextcord.Member, *, reason=None):
  if member == ctx.author:
    return await ctx.send(embed = nextcord.Embed(description = "<:no:993171433981227058> | You can't ban yourself!", color = nextcord.Color.red()))
  elif member.id == 973928310314778625:
    return await ctx.send(embed = nextcord.Embed(description = "<:no:993171433981227058> | You can't ban me!", color = nextcord.Color.red()))
  else:
    await ctx.send(embed=nextcord.Embed(
    		title=f"Вы успешно забанили {member.mention}.",
    		color = 0x2F3136).add_field(
                    name="Модератор:",
                    value=f"{ctx.author.mention}",
                    inline = True).add_field(name="Участник:", value=f"{member.mention}", inline = True).add_field(name="Причина:", value=f"{reason}", inline = True))
    await member.ban(reason=f"{ctx.author.mention}: {reason}")
        
@sudobot.command()
async def kick(ctx, member: nextcord.Member = None, *, reason:str =None):
    await ctx.send(embed = nextcord.Embed(
        description="Извините, но данная функция временно не работает.",
		color = 0x2F3136
	))
    
@sudobot.slash_command(name = "kick", description="Кикает пользователя")
@application_checks.has_permissions(kick_members=True)
async def kickuser(ctx, member: nextcord.Member = None, *, reason:str =None):
  await interaction.send(embed = nextcord.Embed(
      description="Извините, но данная функция временно не работает.",
		color = 0x2F3136
	))


sudobot.run('MTA5NTQxODUyNzg3NzQ1MTg4Nw.G5-bB9.d8DacNUSA-7WX4dFybJbA75vtav_gdZOygTgDA') 

#обычный бот: OTQyMDA1OTg2OTIxNjg1MDcz.Gqtd5g.1_hrK5ZqzZ6oAFIF9aNa0_SJ2Wae7985Vccmn0
#beta: MTA2MzkxMDQ2MDk0NjEyODk4Nw.GEvgOu.ch7lchzRGDrenhS49wY7J_mzpGiLixvstcPLNw
