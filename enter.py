# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk

def ent():
    # главное окно приложения
    window_ent = Tk()
    # заголовок окна
    window_ent.title('Авторизация')
    # размер окна
    window_ent.geometry('450x230+400+150')
    # менять размер
    window_ent.resizable(False, False)

    # шрифты и отступы
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    def clicked():
        output = open('logins.txt','r')
        username = username_entry.get()
        password = password_entry.get()
        while True:
            s = 0
            line =  output.readline()
            if not line:
                break
            username_in_file, password_in_file = line.split() 
            if (username == username_in_file and password == password_in_file):
                window_ent.destroy()
                break
            elif (username != username_in_file or password != password_in_file):
                messagebox.showerror('Ошибка','Неправильный логин или пароль')
                break
        output.close()
        
    # настройка
    main_label = Label(window_ent, text='Вход', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()

    # метка для логина
    username_label = Label(window_ent, text='Имя пользователя', font=label_font , **base_padding)
    username_label.pack()

    # логин
    username_entry = Entry(window_ent, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка пароля
    password_label = Label(window_ent, text='Пароль', font=label_font , **base_padding)
    password_label.pack()

    # пароль
    password_entry = Entry(window_ent, bg='#fff', fg='#444', font=font_entry, show='*')
    password_entry.pack()

    # кнопка Войти
    send_btn = Button(window_ent, text='Войти', command=clicked)
    send_btn.pack(**base_padding)


    # главный цикл
    window_ent.mainloop()
       
