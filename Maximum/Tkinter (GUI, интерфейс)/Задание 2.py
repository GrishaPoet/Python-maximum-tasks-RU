#Время  (Задание №2, Урок 7)
#Задача: Доработайте кликер, сделайте так, чтобы при достижении 20 очков программа “зависала на 2 секунды”.

#Ответ: 

import random
from tkinter import * 
import time 

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
         time.sleep(2)


b = Button(text='Click', font=('Arial, 20'), fg='black', command=check)
b.place(x=200, y=200)
label = Label(text=points, font=('Arial', 15), fg='black')
label.place(x=10, y=10)

window.mainloop()