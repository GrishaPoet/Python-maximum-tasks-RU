#Очень простая задача (Задание №2, Урок 3)
#Задача:Напишите программу, которая принимает сначала 3 названий животных, а потом 3 описаний для животных. 
#После чего случайным образом выбирает одно описание и одного животного и выводит 3 разных комбинации.


#Ответ: 

import random #импортируем библеотеку random
animals = [] #создаём пустые списки
write = [] 
for i in range(3): #создаём цикл
    animals_1 = str(input("Введите название животных: "))
    animals.append(animals_1)
for i in range(3):
    write_1 = str(input("Введите описание животных: "))
    write.append(write_1)
print((random.choice(animals)) +  ''  + (random.choice(write))) #рандомизируем и выводим