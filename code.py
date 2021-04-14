import discord
import random
import os
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from itertools import cycle
import discord.utils
import time
from time import sleep
import base64
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
import warnings
import requests
import unicodedata
import json
import urllib.parse
import urllib.request
import wikipedia
from random import randint
from googlesearch import search
import sys
from pytube import YouTube
import neis


# 선언
words=[]
strname='비행기#7009'

levelmaxima=0
url = 'http://api.openweathermap.org/data/2.5/weather'
v='버전 1.0.0(2021-04-11)'
pv='파이썬 3.6.8 64bit'
rhotkey='report error by !report'
client=commands.Bot(command_prefix='!',help_command=None)
status=cycle(['도움말은 !help',v,pv,rhotkey,'패치노트는 !patch'])
directory=os.path.dirname(__file__)
BASE = "https://youtube.com/results"
token='Nzk5NDUyMTE3NDgzNTIwMDQw.YADxzQ.0UbM02qAQxDQ1HrlHZKcSknef34'
warned=[]

prov_list = [
    {'name':'Seoul','city_id':'1835847'},
    {'name':'Busan','city_id':'1838524'},
    {'name':'Daegu','city_id':'1835329'},
    {'name':'Incheon','city_id':'1843564'},
    {'name':'Gwangju','city_id':'1841811'},
    {'name':'Daejeon','city_id':'1835235'},
    {'name':'Ulsan','city_id':'1833747'},
    {'name':'Sejong','city_id':'1835235'},
    {'name':'Gyeonggi','city_id':'1841610'},
    {'name':'Gangwon','city_id':'1843125'},
    {'name':'Chungcheongbuk','city_id':'1845106'},
    {'name':'Chungcheongnam','city_id':'1845105'},
    {'name':'Jeollabuk','city_id':'1845789'},
    {'name':'Jeollanam','city_id':'1845788'},
    {'name':'Gyeongsangbuk','city_id':'1841597'},
    {'name':'Gyeongsangnam  ','city_id':'1902028'},
    {'name':'Jeju','city_id':'1846266'},
]
tpatch='''
1. 서비스 시작
'''
def it_is_me(ctx):
    return 1

def wiki_summary(arg):
    definition=wikipedia.summary(arg,sentences=3,chars=1000,
    auto_suggest=False,redirect=True)
    return definition

def format_number(number):
    return '{:,d}'.format(number)

def converte_kelvin_to_celsius(k):
    return (k-273.15)

#기본적인 내용

@client.event 
async def on_ready(): 
    change_status.start()
    print("online and ready")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('오류 발생')
        await ctx.send('`Error: Missing required arguments`')
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send('오류 발생')
        await ctx.send('`Error: Command not found`')
    elif isinstance(error,commands.MemberNotFound):
        await ctx.send('오류 발생')
        await ctx.send('`Error: Member not found`')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

@client.command() 
async def ping(ctx):
    n='Normal'
    if(round(client.latency*1000)>200):
        n='Little bit abnormal'
        if(round(client.latency*1000)>300):
            n='Abnormal'
            if(round(client.latency*1000)>500):
                n='Very abnormal'
                if(round(client.latency*1000)>1000):
                    n='WTF'

    embed=discord.Embed(
        title="result",
        description=None,
        color=discord.Color.dark_gray()
    )
    embed.add_field(name="ping(ms)",value=round(client.latency*1000),inline=True)
    embed.add_field(name="real latency(s)", value=round(client.latency), inline=True)
    embed.add_field(name="The bot's result",value=n,inline=True)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed=discord.Embed(
        title="commands",
        description=None,
        color=discord.Color.dark_gray()
    )
    embed.add_field(name='prefix',value='!',inline=True)
    embed.add_field(name="!(개그 요소) (char)",value='answer, fortune',inline=False)
    embed.add_field(name="!(개그 요소)", value='f, x', inline=False)
    embed.add_field(name="!(검색 기능) (char)",value='google, nation, video, wiki, youtube',inline=True)
    embed.add_field(name="!(검색 기능)",value='cbs, corona, meals, weather, 재난안전문자',inline=True)
    embed.add_field(name="!(서버 기능) (int)",value="clear",inline=True)
    embed.add_field(name="!(서버 기능) (char)",value="encode, decode, report",inline=True)
    embed.add_field(name="!(서버 기능)",value="Bot, help, info, name, patch, ping, send, server, 서버, maker, ",inline=True)
    embed.add_field(name='!(어드민 기능)',value='kick, warn',inline=True)
    embed.add_field(name='!(시간 요소)',value='time, clock',inline=True)
    embed.add_field(name='!(다른 요소)',value="dice",inline=True)
    embed.add_field(name='!(개발 중)',value='None',inline=True)
    await ctx.send(embed=embed)

# '''

#개그 요소

@client.command()
async def starforce(ctx,num:int):
    upgrade=0
    downgrade=90
    broken=100
    level=0
    global levelmaxima
    x=0
    while(x<=num):
        chance=random.randrange(1,101)
        if(chance>=upgrade and chance<downgrade):
            if(level>=3):
                upgrade=upgrade+1
                downgrade=downgrade-1
                broken=broken-1
            else:
                upgrade=upgrade+1
                downgrade=downgrade-1
            level=level+1
        elif(chance>=downgrade and chance<broken):
            if(level>=3):
                upgrade=upgrade-1
                downgrade=downgrade+1
                broken=broken+1
            else:
                upgrade=upgrade-1
                downgrade=downgrade+1
            level=level-1
        elif(chance>=broken):
            if(level>levelmaxima):
                levelmaxima=level
            break
    embed=discord.Embed(
        title='Starforce',
        description=None,
        color=discord.Color.blue()
    )
    embed.add_field(name='level',value=str(level),inline=True)
    embed.add_field(name='upgrade chance',value=str(upgrade)+'~'+str(downgrade),inline=True)
    embed.add_field(name='downgrade chance',value=str(downgrade)+'~'+str(broken),inline=True)
    embed.add_field(name='broken chance',value=str(broken)+'~'+str(100),inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=['f'])
async def x(ctx): await ctx.send('x를 눌러 joy를 표하시오.')

@client.command(aliases=['answer','fortune'])
async def _answer(ctx,*,question):
    responses=['Wow','Good.','...',':thinking: :thinking: :thinking: ','WTF',':middle_finger:']
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')

#검색 기능

@client.command()
async def meals(ctx):
    schoolname='백현'
    try:
        client=neis.NeisClient('경기')
        schools=client.search_school(schoolname)
        meals = schools[3].get_weekly_meals(2021,4,8, 2)
        embed=discord.Embed(
            title='급식',
            description='맛있음',
            color=discord.Color.gold()
        )
        for x in range(0,7):
            embed.add_field(name='밥'+str(x+1),value=str(meals[x].menus),inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send('오류:\n`No name such as'+str(schoolname)+'`')

@client.command()
async def video(ctx,*,code):
    link='https://youtu.be/'+code
    yt = YouTube(link)
    embed=discord.Embed(
        title=yt.title,
        description=yt.description,
        color=discord.Color.red()
    )
    minsec=str(int(yt.length/60))+' min '+str(int(yt.length%60))+' sec'
    embed.set_thumbnail(url=yt.thumbnail_url)
    embed.add_field(name='Author',value=yt.author,inline=True)
    embed.add_field(name="Views", value=yt.views, inline=True)
    embed.add_field(name="Length",value=minsec,inline=True)
    embed.add_field(name="Rating",value=yt.rating,inline=True)
    await ctx.send(embed=embed)

@client.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall( r"watch\?v=(\S{11})", htm_content.read().decode())
    for x in range(0,5):
        link='https://youtu.be/'+search_results[x]
        yt = YouTube(link)
        embed=discord.Embed(
            title=yt.title,
            description=yt.description,
            color=discord.Color.red()
        )
        minsec=str(int(yt.length/60))+' min '+str(int(yt.length%60))+' sec'
        embed.set_thumbnail(url=yt.thumbnail_url)
        embed.add_field(name='Author',value=yt.author,inline=True)
        embed.add_field(name="Views", value=yt.views, inline=True)
        embed.add_field(name="Length",value=minsec,inline=True)
        embed.add_field(name="Rating",value=yt.rating,inline=True)
        await ctx.send(embed=embed)

@client.command()
async def wiki(ctx, question):
    search=discord.Embed(title='Searching...',description=wiki_summary(question),color=discord.Color.dark_gray())
    await ctx.send(content=None,embed=search)

@client.command()
async def google(ctx,*,query):
    embed=discord.Embed(
        title='슈퍼컴이 "'+str(query)+'" 에 대해 검색하고 있습니다...',
        description=None,
        color=discord.Color.blue()
    )
    i=1
    for j in search(query, tld="co.in", num=5, stop=5, pause=2):
        embed.add_field(name='link '+str(i),value=str(j),inline=False)
        i=i+1
    await ctx.send(embed=embed)

@client.command()
async def corona(ctx):
    country_data_url = "https://corona.lmao.ninja/v3/covid-19/countries/South%20Korea"
    res = requests.get(country_data_url).text
    country_corona_info = json.loads(res)
    embed=discord.Embed(
        title="South Korea Corona Data",
        description=str(time.strftime('%c', time.localtime(time.time()))),
        color=discord.Color.blue()
    )
    embed.add_field(name="국가",value='South Korea',inline=True)
    embed.add_field(name="추가 확진자", value=str(format_number(country_corona_info["todayCases"])), inline=True)
    embed.add_field(name="추가 사망자",value=str(format_number(country_corona_info["todayDeaths"])),inline=True)
    embed.add_field(name="확진자",value=str(format_number(country_corona_info["cases"])),inline=True)
    embed.add_field(name='사망자',value=str(format_number(country_corona_info["deaths"])),inline=True)
    embed.add_field(name='격리 해제',value=str(format_number(country_corona_info["recovered"])),inline=True)
    embed.add_field(name='격리중',value=str(format_number(country_corona_info["active"])),inline=True)
    await ctx.send(embed=embed)
    global_data_url = "https://corona.lmao.ninja/v3/covid-19/all"
    res = requests.get(global_data_url).text
    country_corona_info = json.loads(res)
    embed=discord.Embed(
        title="Global Corona Data",
        description=str(time.strftime('%c', time.localtime(time.time()))),
        color=discord.Color.blue()
    )
    embed.add_field(name="확진자",value=str(format_number(country_corona_info["cases"])),inline=True)
    embed.add_field(name='사망자',value=str(format_number(country_corona_info["deaths"])),inline=True)
    embed.add_field(name='격리 해제',value=str(format_number(country_corona_info["recovered"])),inline=True)
    embed.add_field(name='격리중',value=str(format_number(country_corona_info["active"])),inline=True)
    await ctx.send(embed=embed)

@client.command()
async def nation(ctx,*,nara):
    try:
        country_data_url = "https://corona.lmao.ninja/v3/covid-19/countries/"+nara
        res = requests.get(country_data_url).text
        country_corona_info = json.loads(res)
        embed=discord.Embed(
            title=nara+" Corona Data",
            description=str(time.strftime('%c', time.localtime(time.time()))),
            color=discord.Color.blue()
        )
        embed.add_field(name="국가",value=nara,inline=True)
        embed.add_field(name="추가 확진자", value=str(format_number(country_corona_info["todayCases"])), inline=True)
        embed.add_field(name="추가 사망자",value=str(format_number(country_corona_info["todayDeaths"])),inline=True)
        embed.add_field(name="확진자",value=str(format_number(country_corona_info["cases"])),inline=True)
        embed.add_field(name='사망자',value=str(format_number(country_corona_info["deaths"])),inline=True)
        embed.add_field(name='격리 해제',value=str(format_number(country_corona_info["recovered"])),inline=True)
        embed.add_field(name='격리중',value=str(format_number(country_corona_info["active"])),inline=True)
        await ctx.send(embed=embed)
    except:
        await ctx.send('오류 발생:')
        await ctx.send('`no such data found as`')
        await ctx.send(nara)

import aiohttp
@client.command(aliases=['재난안전문자'])
async def cbs(ctx):
    CBSList="http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(CBSList) as r:
            data=await r.json()
    embed=discord.Embed(
        title='최근에 발송된 재난안전문자',
        description='전국의 모든 내용을 알려줍니다.',
        color=discord.Color.blue()
    )
    embed.add_field(name='출처',value="http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json",inline=False)
    for i in data[:3]:
        embed.add_field(name=i["SJ"],value=i["CONT"],inline=False)
    await ctx.send(embed=embed)

@client.command()
async def weather(ctx):
    await ctx.send('gathering weather data...')
    weather_info_list = []
    for i in range(len(prov_list)):
        city_id = prov_list[i]['city_id']
        city_name = prov_list[i]['name']
        print(city_name)
        params = dict(
            id=city_id,
            APPID='15d22d08277c1279527a4d79e338a78f',
        )
        sleep(1)
        resp = requests.get(url=url, params=params)
        data = resp.json()
        if(data['cod'] == 429): # blocking error code
            break

        data_main = data['main']
        info = [
            city_id,
            city_name,
            converte_kelvin_to_celsius(data_main['temp_min']), \
            converte_kelvin_to_celsius(data_main['temp']), \
            converte_kelvin_to_celsius(data_main['temp_max']), \
            data_main['pressure'], \
            data_main['humidity']]
        weather_info_list.append(info)
        embed=discord.Embed(
            title=city_name,
            description='Shows the weather in this place',
            color=discord.Color.blue()
        )
        embed.add_field(name='min temp',value=str(converte_kelvin_to_celsius(data_main['temp_min']))+'°C',inline=True)
        embed.add_field(name='temp',value=str(converte_kelvin_to_celsius(data_main['temp']))+'°C',inline=True)
        embed.add_field(name='max temp',value=str(converte_kelvin_to_celsius(data_main['temp_max']))+'°C',inline=True)
        embed.add_field(name='pressure',value=str(data_main['pressure']),inline=True)
        embed.add_field(name='humidity',value=str(data_main['humidity']),inline=True)
        await ctx.send(embed=embed)

@client.command(aliases=['한강'])
async def hangang(ctx):
    data_url='http://hangang.dkserver.wo.tc/'
    res=requests.get(data_url).text
    info=json.loads(res)
    await ctx.send(info["temp"])

#어드민 기능

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)

#서버 기능

@client.command()
async def add(ctx,*,word):
    await ctx.send('words added')
    words.append(word)

@client.command()
async def reset(ctx):
    await ctx.send('words reseted')
    words.clear()

@client.command()
async def wlist(ctx):
    await ctx.send(words)

@client.command(aliases=['초대','invite'])
async def invitebot(ctx,code):
    await ctx.send('https://discord.com/oauth2/authorize?client_id='+code+'&permissions=8&scope=bot')

@client.command(pass_context=True)
async def warn(ctx, user_name: discord.Member):
    if user_name in warned:
        await user_name.kick(reason='You have been warned before.')
    else:
        warned.append(user_name)
        channel = await user_name.create_dm()
        await channel.send("You are got warned! If you get warn one more time, you will be kicked.")

@client.command()
@commands.check(it_is_me)
async def name(ctx): await ctx.send(f'You are {ctx.author}.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def send(ctx,*,arg):
    await ctx.channel.purge(limit=1)
    await ctx.send('@everyone '+arg)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.purge(limit=1)

@client.command(aliases=['server','서버'])
async def _server(ctx):
    name=str(ctx.guild.name)
    description=str(ctx.guild.description)
    owner=str(ctx.guild.owner)
    id=str(ctx.guild.id)
    region=str(ctx.guild.region)
    memberCount=str(ctx.guild.member_count)
    icon=str(ctx.guild.icon_url)
    embed=discord.Embed(
        title="'"+name+"'"+" Sever Information",
        description=description,
        color=discord.Color.dark_gray()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner",value=owner,inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region",value=region,inline=True)
    embed.add_field(name="Member Count",value=memberCount,inline=True)
    await ctx.send(embed=embed)

@client.command()
async def maker(ctx):
    name='junlovecat'
    description='(대충 살려달라는 뜻)'
    owner='JUN#5661'
    region='Korea'
    embed=discord.Embed(
        title="Bot owner's Information",
        description=description,
        color=discord.Color.red()
    )
    embed.add_field(name='name',value=name,inline=True)
    embed.add_field(name="Owner",value=owner,inline=True)
    embed.add_field(name="Country",value=region,inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=['Bot'])
async def info(ctx):
    embed=discord.Embed(
        title="Bot Information",
        description=None,
        color=discord.Color.dark_gray()
    )
    embed.set_thumbnail(url='https://imgur.com/a/V1v8LSl')
    embed.add_field(name="Owner",value='JUN#5661',inline=True)
    embed.add_field(name="Region",value='Korea',inline=True)
    await ctx.send(embed=embed)

@client.command()
async def report(ctx,*,happen):
    await ctx.send('Error reported as')
    await ctx.send(happen)
    print(time.strftime('%c', time.localtime(time.time())),':',happen)

@client.command()
async def encode(ctx,*,intput):
    intputbytes=intput.encode('ascii')
    intputbase64=base64.b64encode(intputbytes)
    output=intputbase64.decode('ascii')
    outputbytes=output.encode('ascii')
    outputbase64=base64.b64encode(outputbytes)
    the_end=outputbase64.decode('ascii')
    await ctx.send(the_end)

@client.command()
async def decode(ctx,*,intput):
    intput_bytes=base64.b64decode(intput)
    output=intput_bytes.decode('ascii')
    output_bytes=base64.b64decode(output)
    the_end=output_bytes.decode('ascii')
    await ctx.send(the_end)

@client.command()
async def patch(ctx):
    await ctx.send(v)
    await ctx.send("패치노트:")
    await ctx.send(tpatch)

#시간 기능

@client.command(aliases=['time'])
async def clock(ctx):
    await ctx.send(time.strftime('%c', time.localtime(time.time())))

#다른 기능

@client.command()
async def dice(ctx):
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    i=1
    while(i<=10000):
        a=random.randrange(1,7)
        if(a==1):a1=a1+1
        elif(a==2):a2=a2+1
        elif(a==3):a3=a3+1
        elif(a==4):a4=a4+1
        elif(a==5):a5=a5+1
        elif(a==6):a6=a6+1
        i=i+1
    
    embed=discord.Embed(
        title="result",
        description=None,
        color=discord.Color.dark_gray()
    )
    embed.add_field(name="1",value=a1,inline=True)
    embed.add_field(name="2",value=a2,inline=True)
    embed.add_field(name="3",value=a3,inline=True)
    embed.add_field(name="4",value=a4,inline=True)
    embed.add_field(name="5",value=a5,inline=True)
    embed.add_field(name="6",value=a6,inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=['del'])
async def delete(ctx,wordsss):
    words.remove(wordsss)
    await ctx.send('words removed')

@client.command()
async def exit(ctx):
    sys.exit()

@client.event
async def on_message(message):
    if(str(message.author)!=strname):
        print(str(message.author)+': ',message.content)
    for i in words:
        if i in message.content:
            if(str(message.author)!=strname):
                if(str(message.content).startswith('!add') or str(message.content).startswith('!del')):
                    print('Not a harmful thing')
                else:
                    await message.delete()
                    await message.channel.send('바른 말 고운 말')
    await client.process_commands(message)

####################################################################################################
client.run('토큰')
# https://discord.com/oauth2/authorize?client_id=799452117483520040&permissions=8&scope=bot 
