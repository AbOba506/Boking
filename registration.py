# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
def reg():
    # главное окно приложения
    window_reg = Tk()
    # заголовок окна
    window_reg.title('Регистрация')
    # размер окна
    window_reg.geometry('450x230')
    # менять размер
    window_reg.resizable(False, False)

    # шрифты и отступы
    font_header = ('Arial', 15)
    font_entry = ('Arial', 12)
    label_font = ('Arial', 11)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    # кнопка Войти
    def clicked():
        output=open('logins.txt','+r')
        # логин и пароль
        username = username_entry.get()
        password = password_entry.get()
        flag = 0
        while True:
            if (len(password)<3):
                flag = -1
                messagebox.showerror('Ошибка','B пароле должно быть не менее 3 трёх символов')
                break
            elif (len(password)>20):
                flag = -1
                messagebox.showerror('Ошибка','B пароле должно быть не более 20 символов')
                break
            elif not re.search("[a-z]", password):
                flag = -1
                messagebox.showerror('Ошибка','В пароле нет строчных латинских букв')
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                messagebox.showerror('Ошибка','В пароле нет заглавных латинских букв')
                break
            elif not re.search("[0-9]", password):
                flag = -1
                messagebox.showerror('Ошибка','В пароле нет цифр')
                break
            elif re.search("\s" , password):
                flag = -1
                messagebox.showerror('Ошибка','В пароле есть пробел')
                break
            elif (len(username)<=2):
                flag = -1
                messagebox.showerror('Ошибка','B логине должно быть не менее 3 трёх символов')
                break
            elif (len(username)>=21):
                flag = -1
                messagebox.showerror('Ошибка','B логине должно быть не более 20 символов')
                break
            elif not re.search("[a-z]", username):
                flag = -1
                messagebox.showerror('Ошибка','В логине нет строчных латинских букв')
                break
            elif not re.search("[A-Z]", username):
                flag = -1
                messagebox.showerror('Ошибка','В логине нет заглавных латинских букв')
                break
            elif re.search("\s" , username):
                flag = -1
                messagebox.showerror('Ошибка','В логине не должно быть пробелов')
                break
            else:
                while True:
                    line =  output.readline()
                    if not line:
                        break
                    username_in_file, password_in_file = line.split() 
                    if (username == username_in_file):
                        flag = -1
                        messagebox.showerror('Ошибка','Такой логин уже занят')
                        window_reg.destroy()
                        reg() 
            if (flag == 0):     
                s = (username+' '+password+"\n")
                output.write(s)
                output.close()
                window_reg.destroy()
                break

    # настройка
    main_label = Label(window_reg, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()

    # метка для логина
    username_label = Label(window_reg, text='Имя пользователя', font=label_font , **base_padding)
    username_label.pack()

    # логин
    username_entry = Entry(window_reg, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка пароля
    password_label = Label(window_reg, text='Пароль', font=label_font , **base_padding)
    password_label.pack()

    # пароль
    password_entry = Entry(window_reg, bg='#fff', fg='#444', font=font_entry, show='*')
    password_entry.pack()

    # кнопка Войти
    send_btn = Button(window_reg, text='Зарегистрироваться', command=clicked)
    send_btn.pack(**base_padding)


    # главный цикл
    window_reg.mainloop()
    