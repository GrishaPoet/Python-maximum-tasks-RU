#Собавья бега (Задание №2, Урок 8)
#Задача: В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. 
# На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и
#  наименьшим количеством очков поменялись местами! Нужно это исправить.

#Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.



#Ответ:

score_dog = [] 
N = int(input('Введите количство собак: '))
print(f'Введёное число: {N}')

for i in range(N):
    score = int(input(f'Введите количество очков для {i + 1 }: '))
    score_dog.append(score)

minimum = score_dog[0]
maxnimum = score_dog[0]

for i in score_dog: 
    if i < minimum:
        minimum = i

for i in score_dog: 
    if i > maxnimum:
        maxnimum = i

for i in range(N):
    if score_dog[i] == minimum:
        score_dog[i] == maxnimum
    elif score_dog[i] == maxnimum:
        score_dog[i] == minimum

print(f'Список: {score_dog}')