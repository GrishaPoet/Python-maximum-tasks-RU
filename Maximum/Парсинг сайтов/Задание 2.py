#Электроника!(Задание №2, Урок 9)
#Задача: Дана следующая ссылка: https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets, спарсите 
#основную информацию об устройствах с этого сайта.



#Ответ:

import requests
from bs4 import BeautifulSoup
import lxml
 
url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'
 
soup = BeautifulSoup(requests.get(url).text, "lxml")
list_rows = soup.select_one("div.ecomerce-items-ajax")['data-items']
print(list_rows)