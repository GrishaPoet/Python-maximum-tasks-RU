#Лотерея!(Задание №1, Урок 8)
#Задача: ДНапишите программу с графическим интерфейсом. В окне программы должна располагаться надпись: 
# “ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!” и кнопка “ПОЛУЧИТЬ ВЫЙГРЫШ!”. При нажатии на кнопку текст меняется на 
# “Чтобы забрать выйгрыш необходимо внести 1000руб.” При этом закрыть окно крестиком нельзя.



#Ответ: 

from tkinter import *

def destroy():
    text.config(text = 'Чтобы забрать выйгрыш необходимо внести 1000руб.',
             font=("Arial Bold", 20))
    c.destroy()

window = Tk()
window.geometry('900x300')
window.resizable(width=False, height=False)
window.config(bg='black')
text = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', fg='green', bg='black')
text.place(x=100, y=100, width=700, height=100)
count_text = Label(text='10', fg='green', bg='black', font=('Arial', 20))
c = Button(text="ПОЛУЧИТЬ ВЫЙГРЫШ!", font=("Arial", 20), fg='black', bg="green", command=destroy)
c.place(x=290, y=200)
с = Label(text='10', fg='green', bg='black', font=('Arial', 20))

window.mainloop()