import discord
import random
import asyncio
import aiohttp
import json
import pickle
import requests
import os
import make

def mamka_api(): 
  response = requests.get("https://api.yomomma.info/")
  return response.text
  mama=response.text
  
discord.__version__
#команды в отдельном файле 
commands_dictionary= 'command.data'
#чтение из этого файла
f = open(commands_dictionary, 'rb')
# и наша таблица со списком команд
commands = pickle.load(f)
imgList = os.listdir("C:/pytnon_apps/discord bot/ALL_IMAGES/")

TOKEN = 'NDg3MjQ2MTUxODQ2OTg1NzM5.DnkrlA.OhEKAtXgTRtrArYaAfccYYzlNrU'
client = discord.Client()
replies={'Аниме':'😊','Amd':'😍','Intel':'💩','Бот':'😎','Osu':'🏳️‍🌈','Осу':'🏳️‍🌈'}
Answer = ('Отстань от меня!','Я занят, не приставай','Информация обо мне доступена по команде !about','DORARARARARARARA!','Break through and beat you up!','Watch your mouth!')
@client.event
async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        elif message.content =='!new':
          msg = ('{0.author.mention}'+ input("Введите текст: ")).format(message)
          await client.send_message(message.channel, msg)
        elif message.content.startswith('!yomama'):
          msg = ('Твоя мамка'+mamka_api()[16:-3] +''.format(message) )
          await client.send_message(message.channel, msg)
        elif client.user.mentioned_in(message) and message.mention_everyone is False:
          msg =random.choice(Answer)
          await client.send_message(message.channel, msg)
        for item in commands:
            if message.content ==item:
                msg = commands[item].format(message)
                await client.send_message(message.channel, msg)
        for item in imgList:
          if message.content =='!'+item[0:-4]:
            imgString = item # выбирает нужный
            path = "C:/pytnon_apps/discord bot/ALL_IMAGES/" + imgString 
            await client.send_file(message.channel, path) # отправляет сообщение в канал
        for item in replies:
          if message.content.startswith(item):
            await client.add_reaction(message,replies[item])


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDg3MjQ2MTUxODQ2OTg1NzM5.DnkrlA.OhEKAtXgTRtrArYaAfccYYzlNrU')
