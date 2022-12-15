#Цвет  (Задание №1, Урок 7)
#Задача:Доработайте кликер. Сделайте так, чтобы при достижении 20 очков цвет кнопки менялся.

#Ответ: 

import random
from tkinter import * 

window = Tk()
window.geometry('700x500')
window.title('Clickers')
points = 0 

def check(): 
    global points
    b.place(x=random.randint(1,100), y=random.randint(1,150))
    points += 1 
    label['text'] = points

    if points == 20:
         b['bg'] = 'orange'


b = Button(text='Click', font=('Arial, 20'), fg='black', command=check)
b.place(x=200, y=200)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)

window.mainloop()