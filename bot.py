import telebot;
from bs4 import BeautifulSoup
import requests;
import os;


def filedown():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    page = requests.get("https://www.butb.by/shedule/lesoproduktsiya/eshche-pod-drevesinu/", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find('div', class_='timetables-market__items active')
    for x in table.find_all('a'):
        links = []
        links.append('https://www.butb.by' + x['href'])

    for x in links:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
        r = requests.get(x, allow_redirects=True, headers=headers)
        open('lotfile.xls', 'wb').write(r.content)

bot = telebot.TeleBot('5360706191:AAHfKeQpLaZedHb4CxGu7oRbX1VrJWkPwm4');
@bot.message_handler(commands=['start', 'getfile'])
def start_message(message):

  def getfile(message):
    doc = open('lotfile.xls', 'rb')
    bot.send_document(message.chat.id, doc)


  if (message.text == '/start'):
    bot.send_message(message.chat.id,"Привет ✌️ ")
  elif message.text == '/getfile':
    bot.send_message(message.chat.id, "File")
    filedown()
    getfile(message)
  else:
    bot.send_message(message.chat.id, "Какая-то хуйня")
bot.infinity_polling(interval=0, timeout=20)
