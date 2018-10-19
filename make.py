import pickle
import discord
import os

def com_list():
    commands_dictionary= 'command.data'
    commands = { '!hello':'Hello {0.author.mention}','!about': 'Бот в процессе разработки. функции будут постепенно добавляться. Сейчас работают следующие функции:!hello, !about, !img ,','!img':'cписок изображений :' + str(os.listdir("C:/pytnon_apps/discord bot/ALL_IMAGES/"))};
    f = open(commands_dictionary, 'wb')
    pickle.dump(commands, f)
    f.close()
    
com_list() 
