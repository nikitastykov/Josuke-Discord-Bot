import discord
import random
import asyncio
import aiohttp
import json
import pickle
import requests
import os
import make

  
discord.__version__
#команды в отдельном файле 
commands_dictionary= 'command.data'
#чтение из этого файла
f = open(commands_dictionary, 'rb')
# и наша таблица со списком команд
commands = pickle.load(f)
imgList = os.listdir("IMAGES PATH HERE")

TOKEN = 'TOKEN HERE'
client = discord.Client()
replies={'Amd':'😍','Бот':'😎'} # добавляет эмоцию к посту
Answer = ('Отстань от меня!','Я занят, не приставай','Информация обо мне доступена по команде !about','DORARARARARARARA!','Break through and beat you up!','Watch your mouth!')
@client.event
async def on_message(message):
        # чтобы бот не отвечал себе сам
        if message.author == client.user:
            return
        elif message.content =='!new':
          msg = ('{0.author.mention}'+ input("Введите текст: ")).format(message)
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
            path = "IMAGES PATH" + imgString 
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

client.run(TOKEN)
