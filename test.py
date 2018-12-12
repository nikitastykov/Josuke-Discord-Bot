#Файл для тестов всяких элементов бота

import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
import lxml
import re
import string

#кусочек паучка для получения последних сообщений 
def d2rucrawl(url):
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
    data=activity
    text_string2 = str(data).lower()
    match_pattern2 = re.findall(r'\b[а-я]{3,15}\b', text_string2)
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
    return 'Никнейм: ' + username.replace(' ','')[2:-1] + ', Сообщения: '+ messagesn[1:-1] +', Симпатии: ' + likes[1:-1]+' Часто используемые слова - за последние 100 сообщений '+ activity_end +' Аватар: '+'https://dota2.ru/'+str(img_c)[2:-4]
