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
    html = urlopen(url+'activity/')

    soup = BeautifulSoup(html, 'lxml')
    type(soup)

    rows4 = soup.find_all('div',class_='text-medium')
    str_cells4 = str(rows4)
    activity = BeautifulSoup(str_cells4, "lxml").get_text()
    return activity



a='https://dota2.ru/forum/members/kremennik.4337/'

data=d2rucrawl(a)
#расчет частоты использования слов
text_string2 = data.lower()
#match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
match_pattern2 = re.findall(r'\b[а-я]{3,15}\b', text_string2)
frequency2 = {}
for word in match_pattern2:
    count = frequency2.get(word,0)
    frequency2[word] = count + 1
     
frequency_list2 = frequency2.keys()
 
for words in frequency_list2:
    if frequency2[words] >2:
        print (words, frequency2[words])
