from bs4 import BeautifulSoup as bs
from config import phrases
import requests
import datetime

# skills
def joke():
    response = requests.get('https://www.anekdot.ru/random/anekdot')
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        anek = soup.find_all('div', class_='topicbox')[
            1].find('div', class_="text").text
        return anek
    else:
        return phrases["not_joke"]


def ctime():
    now = datetime.datetime.now()
    response = f"Сейчас {str(now.hour)}:{str(now.minute)}"
    return response


def news():
    response = requests.get('https://ria.ru/politics/')
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        link = soup.find_all('a', class_='list-item__title')[1].attrs["href"]
        new_response = requests.get(link)
        new_soup = bs(new_response.text, 'html.parser')
        new_texts = new_soup.find_all('div', class_='article__text')
        response = ''
        for text in new_texts:
            response += text.text
        return response
    else:
        return phrases["not_news"]


def hello():
    return phrases['hi']


def goodbye():
    return phrases["end"]


def no():
    return phrases["no"]


skills = {
    "joke": joke,
    "news": news,
    "ctime": ctime,
    "hello": hello,
    "goodbye": goodbye,
    "no": no
}