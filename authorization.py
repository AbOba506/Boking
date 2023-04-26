# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from registration import reg
from enter import ent

# главное окно приложения
window_auth = Tk()
# заголовок окна
window_auth.title('Авторизация')
# размер окна
window_auth.geometry('450x230+400+150')
# менять размер
window_auth.resizable(False, False)

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def clicked_enter():
    window_auth.destroy()
    ent()

def clicked_reg():
    window_auth.destroy()
    reg()


# настройка
main_label = Label(window_auth, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# кнопка Войти
send_btn = Button(window_auth, text='Вход', command=clicked_enter, borderwidth=5, width=15)
send_btn.pack(**base_padding)

# кнопка Войти
send_btv = Button(window_auth, text='Регистрация', command=clicked_reg, borderwidth=5, width=15)
send_btv.pack(**base_padding)

# главный цикл
window_auth.mainloop()