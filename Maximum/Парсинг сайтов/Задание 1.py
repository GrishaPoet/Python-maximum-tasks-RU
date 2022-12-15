#Колумбия!(Задание №1, Урок 9)
#Задача: ДДан несложный пример HTML-страницы: http://www.columbia.edu/~fdc/sample.html

#Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта 
# (они заключены в теги h3).



#Ответ:

import requests, re 
print(re.findall('<h3.*>(.+)</h3>', requests.get('http://www.columbia.edu/~fdc/sample.html').text, flags=re.I))