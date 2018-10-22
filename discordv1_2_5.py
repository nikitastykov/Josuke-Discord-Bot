import discord
import random
import asyncio
import os
import sqlite3

discord.__version__
imgList = os.listdir("IMG FULL PATH HERE")

TOKEN = 'TOKEN HERE'

client = discord.Client()
connection = sqlite3.connect("replies.db")
cursor = connection.cursor()

cursor.execute("SELECT ask,answer FROM command")
commands=cursor.fetchall()


cursor.execute("SELECT * FROM replies")
result=cursor.fetchall()


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
            msg = ('cписок изображений :' + str(os.listdir("IMG FULL PATH HERE"))).format(message)
            await client.send_message(message.channel, msg)
        for item in commands:
            if message.content ==item[0]:
                msg = item[1].format(message)
                await client.send_message(message.channel, msg)
        for item in imgList:
          if message.content =='!'+item[0:-4]:
            imgString = item # выбирает нужный
            path = "IMG FULL PATH HERE" + imgString 
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

client.run('TOKEN HERE')
