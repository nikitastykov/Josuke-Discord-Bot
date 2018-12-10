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

def d2rucrawl(url):
    html = urlopen(url)

    soup = BeautifulSoup(html, 'lxml')
    type(soup)

    rows = soup.find_all('div',class_='dropdown')
    str_cells = str(rows)
    username = BeautifulSoup(str_cells, "lxml").get_text()
    #rows2 = soup.find_all('h4',class_='minor-heading') #,id_="user-posts-count"
    rows2 = soup.find_all('span',id="user-posts-count")
    str_cells2 = str(rows2)
    messagesn = BeautifulSoup(str_cells2, "lxml").get_text()

    img = soup.find_all('img',class_='my')
    return 'Никнейм: ' + username.replace(' ','')[1:-1] + ', Сообщения: '+ messagesn[1:-1]+' Аватар: '+'https://dota2.ru'+str(img)[39:-4]

discord.__version__
imglist = os.listdir("IMG PATH HERE")

TOKEN = 'TOKEN HERE'

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


Answer = ('Отстань от меня!','Я занят, не приставай','Информация обо мне доступена по команде !about','DORARARARARARARA!','Break through and beat you up!','Watch your mouth!')
@client.event
async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        elif client.user.mentioned_in(message) and message.mention_everyone is False:
          msg =random.choice(Answer)
          await client.send_message(message.channel, msg)
        elif message.content =='!img':
            msg = ('cписок изображений : ' +', '.join(new) ).format(message)
            await client.send_message(message.channel, msg)
        elif message.content =='!d2runame':
            msg = d2rucrawl('LINK HERE').format(message)
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
