#Ещё одна кнопка  (Задание №3, Урок 7)
#Задача: ДДобавьте в кликер ещё одну кнопку, которая тоже будет прыгать каждый раз, 
#когда на неё нажимаешь. Сделайте так, чтобы при нажатии на одну из кнопок 
#более 10-ти раз и при отсутствии нажатия на другую кнопку, та кнопка, на которую не 
#нажимали меняла текст на “Ну пожалуйста image_description”.



#Ответ: 

from tkinter import *
from random import *

points_b1 = 0
points_b2 = 0
points = 0

def but_change(b):
    b['text'] = 'Ну пожалуйста'
    b['bg'] = 'blue'
    b['fg'] = 'white'
    global points_b1, points_b2
    points_b1, points_b2 = 0, 0

def points_update():
    global points
    points += 1
    label['text'] = f'Ваши очки: {points}'

def b1_func():
    points_update()
    b1.place(x=randint(1, 500), y=randint(1, 550))
    global points_b1
    global points_b2
    points_b1 += 1
    points_b2 -= points_b2

if points_b1 >= 10:
    but_change(b2)
else:
    b1['text'] = '>НАЖМИ<'
    b1['bg'] = 'green'
    b1['fg'] = 'black'

def b2_func():
    points_update()
    b2.place(x=randint(1, 500), y=randint(1, 550))
    global points_b1
    global points_b2
    points_b2 += 1
    points_b1 -= points_b1

if points_b2 >= 10:
    but_change(b1)
else:
    b2['text'] = '>ТРОНЬ<'
    b2['bg'] = 'yellow'
    b2['fg'] = 'black'





win = Tk()
win.geometry('800x600+250+80')
win.title('Кликер :D')

b1 = Button(text='>НАЖМИ<', font=('Calibri', 15), bg='green', command=b1_func)
b2 = Button(text='>ТРОНЬ<', font=('Calibri', 15), bg='yellow', command=b2_func)

b1.place(x=150, y=200)
b2.place(x=450, y=200)

label = Label(text=f'Ваши очки: {points}', fg='black', font=('Calibri', 10))
label.place(x=10, y=10)


win.mainloop()