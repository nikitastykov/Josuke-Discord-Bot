__version__ = "$ Josuke_bot:v01_2_8 0. $"

import discord
import random
import asyncio
import os
import sqlite3
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
import lxml
import re
import time
import apiai
import json

def d2rucrawl(url):
    print('работаю')
    pages=1
    activity=[]    

    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    type(soup)
    rows = soup.find_all('div',class_='dropdown')
    str_cells = str(rows)
    username = BeautifulSoup(str_cells, "lxml").get_text()
    rows2 = soup.find_all('span',id="user-posts-count")
    str_cells2 = str(rows2)
    messagesn = BeautifulSoup(str_cells2, "lxml").get_text()
    rows3 = soup.find_all('span',class_="points")
    str_cells3 = str(rows3)
    likes = BeautifulSoup(str_cells3, "lxml").get_text()
    img = soup.find_all('img',class_='my')
    img_a=(str(img).split('/')[1:7])
    img_b=[i+'/'for i in img_a]
    img_c=[''.join(img_b)]

    while pages <11 and pages !=0: #блок расчета колличества постов
        html = urlopen(url+'activity/page-'+str(pages))
        soup = BeautifulSoup(html, 'lxml')
        type(soup)
        rows4 = soup.find_all('div',class_='text-medium')
        str_cells4 = str(rows4)
        activ = BeautifulSoup(str_cells4, "lxml").get_text()
        activity.append(activ)
        pages+=1
        time.sleep( 0.1 )
        print('Страница'+str(pages))
    data=activity
    text_string2 = str(data).lower()
    match_pattern2 = re.findall(r'\b[а-я]{4,15}\b', text_string2)
    frequency2 = {}
    for word in match_pattern2:
      count = frequency2.get(word,0)
      frequency2[word] = count + 1
    frequency_list2 = frequency2.keys()
    activity_mess=[]
    for words in frequency_list2:
        if frequency2[words] >5:
          activity_mess.append(str(words) +': '+ str(frequency2[words]))

    activity_end=', '.join(activity_mess)
    return 'Никнейм: ' + username.replace(' ','')[2:-1] + ', Сообщения: '+ messagesn[1:-1] +', Симпатии: ' + likes[1:-1]+' Часто используемые слова  за последние 100 сообщений - '+ activity_end +' Аватар: '+'https://dota2.ru/'+str(img_c)[2:-4]

def textMessage(update):
    request = apiai.ApiAI('DIALOGFLOAPI').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'Josuke' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update #message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        return response
    else:
        return 'Я Вас не совсем понял!'


discord.__version__
imglist = os.listdir("IMAGES PATH")

TOKEN = 'DISCORD TOKEN'

client = discord.Client()
connection = sqlite3.connect("replies.db")
cursor = connection.cursor()

cursor.execute("SELECT ask,answer FROM command")
commands=cursor.fetchall()


cursor.execute("SELECT * FROM replies")
result=cursor.fetchall()

new=[]
for i in imglist:
    new.append('!' +i[0:-4])


#Answer = ('Отстань от меня!','Я занят, не приставай','Информация обо мне доступена по команде !about','DORARARARARARARA!','Break through and beat you up!','Watch your mouth!')
@client.event
async def on_message(message):
     
        if message.author == client.user:
            return
        #elif client.user.mentioned_in(message) and message.mention_everyone is False:
          #msg =random.choice(Answer)
          #await client.send_message(message.channel, msg)
        elif client.user.mentioned_in(message) and message.mention_everyone is False:
            msg =textMessage(message.content[22:])
            await client.send_message(message.channel, msg)
        elif message.content =='!img':
            msg = ('cписок изображений : ' +', '.join(new) ).format(message)
            await client.send_message(message.channel, msg)
        elif message.content.startswith ('!d2'):
            u_input=message.content[3:]
            msg = d2rucrawl(u_input).format(message)
            await client.send_message(message.channel, msg)
        for item in commands:
            if message.content ==item[0]:
                msg = item[1].format(message)
                await client.send_message(message.channel, msg)
        for item in imglist:
          if message.content =='!'+item[0:-4]:
            imgString = item # выбирает нужный
            path = "C:/pytnon_apps/discord bot/ALL_IMAGES/" + imgString 
            await client.send_file(message.channel, path) # отправляет сообщение в канал
        for item in result:
          if message.content.startswith(item):
            await client.add_reaction(message,item[1])



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
