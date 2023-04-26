# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from main import main
from enter import ent

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def data():
    # функция нажатия кнопки заполнить данные
    def data_clicked():
        rez = open('logins.txt', 'a')
        name = name_entry.get()
        age = age_entry.get()
        driving_experience = driving_experience_entry.get()
        criminal = criminal_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        card  = card_entry.get()
        s = ' ' + name + ' ' + age + ' ' + driving_experience + ' ' + criminal + ' ' + phone + ' ' + email + ' ' + card + '\n'
        rez.write(s)
        rez.close()
        window_data.destroy()
    header_padding_1 = {'padx': 10, 'pady': 7}
    # главное окно приложения
    window_data = Tk()
    # заголовок окна
    window_data.title('Регистрация')
    # размер окна
    window_data.geometry('450x330+400+150')
    # менять размер
    window_data.resizable(False, False)
        
    # настройка
    data_label = Label(window_data, text='Заполнение данных', font=('Arial', 12), justify=CENTER, **header_padding_1)
    data_label.grid(row=0, column=1)

    # метка для имени
    name_label = Label(window_data, text='Имя', font=('Arial', 12), **header_padding_1)
    name_label.grid(row=1, column=0)

    # поле имя
    name_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    name_entry.grid(row=1, column=1)

    # метка возраста
    age_label = Label(window_data, text='Возраст', font=('Arial', 12), **header_padding_1)
    age_label.grid(row=2, column=0)

    # возраст
    age_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    age_entry.grid(row=2, column=1)

    # метка опыта вождения
    driving_experience_label = Label(window_data, text='Опыт Вождения', font=('Arial', 12), **header_padding_1)
    driving_experience_label.grid(row=3, column=0)

    # опыт вождения
    driving_experience_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    driving_experience_entry.grid(row=3, column=1)

    # метка Судимость
    criminal_label = Label(window_data, text='Судимость', font=('Arial', 12), **header_padding_1)
    criminal_label.grid(row=4, column=0)

    # Судимость
    criminal_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    criminal_entry.grid(row=4, column=1)

    # метка номер телефона
    phone_label = Label(window_data, text='Номер телефона', font=('Arial', 12), **header_padding_1)
    phone_label.grid(row=5, column=0)

    # номер телефона
    phone_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    phone_entry.grid(row=5, column=1)

    # метка E-mail
    email_label = Label(window_data, text='E-mail', font=('Arial', 12), **header_padding_1)
    email_label.grid(row=6, column=0)

    # E-mail
    email_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    email_entry.grid(row=6, column=1)

    # метка номер карты
    card_label = Label(window_data, text='Card', font=('Arial', 12), **header_padding_1)
    card_label.grid(row=7, column=0)

    # номер карты
    card_entry = Entry(window_data, bg='#fff', fg='#444', font=('Arial', 12))
    card_entry.grid(row=7, column=1)

    # кнопка Заполнить данные
    send_btn = Button(window_data, text='Заполнить данные', command=data_clicked)
    send_btn.grid(row=8, column=1)



def reg():
    # главное окно приложения
    window_reg = Tk()
    # заголовок окна
    window_reg.title('Регистрация')
    # размер окна
    window_reg.geometry('450x230+400+150')
    # менять размер
    window_reg.resizable(False, False)

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
                    username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card = line.split() 
                    if (username == username_in_file):
                        flag = -1
                        messagebox.showerror('Ошибка','Такой логин уже занят')
                        window_reg.destroy()
                        reg() 
            if (flag == 0):     
                s = (username+' '+password)
                output.write(s)
                output.close()
                window_reg.destroy()
                break
        data()

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
    ent()
