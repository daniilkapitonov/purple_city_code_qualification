#!/usr/bin/env python3

print("Content-type: text/html")
print()
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# Основной класс
class Currency:
 # Ссылка на нужную страницу
 DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw:1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=доллар+к+рублю&oq=доллар+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
 # Заголовки для передачи вместе с URL
 headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

 current_converted_price = 0
 difference = 5 # Разница после которой будет отправлено сообщение на почту

 def __init__(self):
  # Установка курса валюты при создании объекта
  self.current_converted_price = float(self.get_currency_price().replace(",", "."))

 # Метод для получения курса валюты
 def get_currency_price(self):
  # Парсим всю страницу
  full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

  # Разбираем через BeautifulSoup
  soup = BeautifulSoup(full_page.content, 'html.parser')

  # Получаем нужное для нас значение и возвращаем его
  convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
  return convert[0].text

  print("<p> Сейчас курс: 1 доллар =  + str(currency)<p>")
  time.sleep(3) # Засыпание программы на 3 секунды
  self.check_currency()

  server.quit()

# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()