#Очень простая задача (Задание №3, Урок 3)
#Задача: Напишите программу, которая заполняет 
#список случайными числами от 0 до 5 (30 итераций). После этого посчитайте количество пятерок в списке.


#Ответ: 

import random 
a = [random.randint(0, 5) for i in range(30)]
print(*a); b = ((a.count(5))); print(f'Количество пятёрок в списке: {b}')