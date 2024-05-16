import config
import time
import nextcord
from nextcord.ext import commands, tasks
import asyncio
import random
from nextcord import Member
 

print("CMW Corporation")

hello_words = ["привет", "здарова", "hello", "hi", "здравствуйте"]

imgscats = ['https://i.postimg.cc/bvCT7tzC/Screenshot-20220629-173035.jpg',
            'https://i.postimg.cc/28S56LmF/photo-2022-06-28-21-50-18.jpg', 
            'https://i.postimg.cc/W3SvLSDR/photo-2022-06-30-23-56-14.jpg',
            'https://i.postimg.cc/N0tYP4Yt/IMG-f89a0f657343f2015c3ece7a23e78b57-V.jpg',
            'https://i.postimg.cc/bvjPkKmk/1561011173-8-1.jpg',
            'https://i.postimg.cc/pLb46KKt/786fc0798233006257d41dc0132f6387-1.jpg']

imgdogs = ['https://i.postimg.cc/Bnm6RHsb/shutterstock-231364474-2.jpg', 'https://i.postimg.cc/TwD3ysb5/0e26b1b65946ee36fac9605ae67e4ac8.jpg', 'https://i.postimg.cc/zXjXRKy7/d381cb1cdcf05cbc6dce920f76ee7555.jpg', 'https://i.postimg.cc/MppZ0HRS/1936556.jpg']

word = ['Да!', 'Конечно!', 'Нет.', 'Не знаю...', 'Спроси по-позже.']

client = commands.Bot(command_prefix = "$sudo ", strip_after_prefix = True, intents=nextcord.Intents.all())
client.persistent_views_added = False
client.remove_command("help")
 


@client.event
async def on_ready(): 
    print('Бот запущен')

    await client.change_presence( status = nextcord.Status.online, activity = nextcord.Game('Сильные тормоза'))
 
@client.command()
async def clear(ctx, amount: int=100):
  amount_purged = await ctx.channel.purge(limit=amount)
  await ctx.send(embed = nextcord.Embed(
    title=f" <:yes:993171492563079260>    |   Успешно удалено `{len (amount_purged)}` сообщений!",
		color = 0x2F3136
	), delete_after = 6)
 

@client.command()
async def help(ctx):
    await ctx.send('1. $sudo hack {Пользователь} - Взламывает пользователя (не по-настоящему)')
    await ctx.send('2. $sudo invite - генерирует ссылку на бота')
    await ctx.send('3. $sudo ver - показывает какая версия')
    await ctx.send('4. $sudo cat - показывает рандомную картинку с котом.')
    await ctx.send('5. $sudo dog - показывает рандомную картинку c собакой')
    await ctx.send('6. $sudo ban {Пользователь} - Банит пользователя')
    await ctx.send('7. $sudo kick {Пользователь} - Кикает пользователя')
    await ctx.send('8. $sudo clear - Чистит чат')
 
@client.command()
async def cat(ctx):
    await ctx.send(random.choice(imgscats))

#@client.command()
#async def word(ctx):
 #   await ctx.send(random.choice(word))

@client.command()
async def hack(ctx):
    await ctx.send("Бот недоступен.")

@client.command()
async def ver(ctx):
    await ctx.send('Промежуточное обновление 0.6.5')

@client.command()
async def invite(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=942005986921685073&permissions=274879028294&scope=client')

@client.command()
async def dog(ctx):
    await ctx.send(random.choice(imgdogs))


@client.command()
async def ban(ctx, member: nextcord.Member = None, time = None, *, reason: str = None):
    async def unb(member):
        users = await ctx.guild.bans()
        for ban_user in users:
            if ban_user.user == member:
                await ctx.guild.unban(ban_user.user)
                
    if member:
        if time: 
            time_letter = time[-1:] 
            time_numbers = int(time[:-1]) 
            
            def t(time_letter): 
                if time_letter == 's':
                    return 1
                if time_letter == 'm':
                    return 60
                if time_letter == 'h':
                    return 60*60
                if time_letter == 'd':
                    return 60*60*24
            if reason:
                await member.ban(reason=reason)
                await ctx.send(embed=nextcord.Embed(description=f'Пользователь {member.mention} был забанен \nВремя: {time} \nПричина: {reason}' ))
                
                await asyncio.sleep(time_numbers*t(time_letter))
                
                await unb(member)
                await ctx.send(f'Польнзователь {member.mention} разбанен')
            else:
                await member.ban()
                await ctx.send(embed=nextcord.Embed(description=f'Пользователь {member.mention} был забанен \nВремя: {time}'))
                
                await asyncio.sleep(time_numbers*t(time_letter))
                
                await unb(member)
                await ctx.send(f'Польнзователь {member.mention} разбанен')
        else:
            await member.ban()
            await ctx.send(embed=nextcord.Embed(description=f'Пользователь {member.mention} был забанен'))
    else: 
        await ctx.send('Введите имя пользователя')
        
 
@client.command()
async def unban(ctx, id_: int = None):
    if id_:
        banned_users = await ctx.guild.bans()
        member_full = client.get_user(id=id_)
        for ban in banned_users:
            if ban.user == member_full:
                await ctx.guild.unban(ban.user)
        await ctx.send('Пользователь разбанен')
    else:
        await ctx.send('Введите айди')
        
        
@client.command()
async def kick(ctx, member: nextcord.Member = None, *, reason:str =None):
    if member:
        if reason:
            await member.kick(reason=reason)
            await ctx.send(embed=nextcord.Embed(description=f'Пользователь {member.mention} был кикнут \nПричина: {reason}' ))
        else:
            await member.kick()
            await ctx.send(embed=nextcord.Embed(description=f'Пользователь {member.mention} был кикнут'))
    else: 
        await ctx.send('Введите имя пользователя')
 

client.run(my_secret)
