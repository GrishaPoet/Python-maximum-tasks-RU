#Калькулятор  (Задание №3, Урок 6)
#Задача:Допишите калькулятор, добавьте функции умножения и деления. Все ответы должны сохраняться в текстовый документ.
#Оберните код калькулятора в функцию. Которая принимает три аргумента: два числа и операция.

#Ответ: 

def calc(a,b, operand):
    if operand == '+':
        res = a + b
    elif operand == '-':
        res = a - b
    elif operand == '*':
        res = a * b
    elif operand == '/':
        res = a / b 
    else:
        res = 'Извините, но такой операции нет в калькуляторе.'
    return res

num1 = int(input('Введите число:'))
num2 = int(input('Введите число:'))
opel = input('введите операцию:')
toga= calc(num1, num2, opel)
print(toga)

file = open('calculations.txt', 'a')
file.write(f'{toga}' + '\n')