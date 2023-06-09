# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from enter import Enter
import sqlite3

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}
header_padding_1 = {'padx': 10, 'pady': 7}
color0 = "#ffffff"
color1 = "#4456F0"

class Data:
    def __init__(self):
        self.root = Tk()
        self.root.title('Авторизация')
        self.root.geometry('450x330+400+150')
        self.root.resizable=(False, False)
    # Виджеты
        self.data_label = Label(self.root, text='Заполнение данных', font=('Arial', 12), justify=CENTER, **header_padding_1)
        self.name_label = Label(self.root, text='Имя *', font=('Arial', 12), **header_padding_1)
        self.name_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.age_label = Label(self.root, text='Возраст *', font=('Arial', 12), **header_padding_1)
        self.age_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.driving_experience_label = Label(self.root, text='Опыт Вождения *', font=('Arial', 12), **header_padding_1)
        self.driving_experience_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.criminal_label = Label(self.root, text='Судимость *', font=('Arial', 12), **header_padding_1)
        self.criminal_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.phone_label = Label(self.root, text='Номер телефона *', font=('Arial', 12), **header_padding_1)
        self.phone_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.email_label = Label(self.root, text='E-mail *', font=('Arial', 12), **header_padding_1)
        self.email_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.card_label = Label(self.root, text='Card *', font=('Arial', 12), **header_padding_1)
        self.card_entry = Entry(self.root, bg='#fff', fg='#444', font=('Arial', 12), highlightthickness=1, relief='solid')
        self.send_btn = Button(self.root, text='Заполнить данные', command=self.data_clicked, borderwidth=3, bg=color1, fg=color0)

    def draw_widjets(self):
        self.data_label.grid(row=0, column=1)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.age_label.grid(row=2, column=0)
        self.age_entry.grid(row=2, column=1)
        self.driving_experience_label.grid(row=3, column=0)
        self.driving_experience_entry.grid(row=3, column=1)
        self.criminal_label.grid(row=4, column=0)
        self.criminal_entry.grid(row=4, column=1)
        self.phone_label.grid(row=5, column=0)
        self.phone_entry.grid(row=5, column=1)
        self.email_label.grid(row=6, column=0)
        self.email_entry.grid(row=6, column=1)
        self.card_label.grid(row=7, column=0)
        self.card_entry.grid(row=7, column=1)
        self.send_btn.grid(row=8, column=1)

    def run(self):
        self.draw_widjets()
        self.root.mainloop()

    def data_clicked(self):
        rez = open('logins.txt', 'a')
        name = self.name_entry.get()
        age = self.age_entry.get()
        driving_experience = self.driving_experience_entry.get()
        criminal = self.criminal_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        card  = self.card_entry.get()

        s = ' ' + name + ' ' + age + ' ' + driving_experience + ' ' + criminal + ' ' + phone + ' ' + email + ' ' + card + '\n'
        rez.write(s)
        rez.close()
        try:
            sqlite_connection = sqlite3.connect('data.db')
            cursor = sqlite_connection.cursor()
            f_read = open("logins.txt", "r")
            last_line = f_read.readlines()[-1]
            username, password, name, age, driving_experience, criminal, phone, email, card = last_line.split()
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS user (
                                        username TEXT NOT NULL,
                                        password TEXT NOT NULL,
                                        name TEXT NOT NULL,
                                        age INT NOT NULL,
                                        driving_experience INT NOT NULL,
                                        criminal TEXT NOT NULL,
                                        phone TEXT NOT NULL,
                                        email TEXT NOT NULL,
                                        card TEXT NOT NULL,
                                        civic INT NOT NULL, 
                                        nsx INT NOT NULL,
                                        s2000 INT NOT NULL,
                                        prelude INT NOT NULL,
                                        stagea INT NOT NULL,
                                        skyline INT NOT NULL,
                                        silvia INT NOT NULL,
                                        GTR INT NOT NULL,
                                        p911 INT NOT NULL,
                                        cayenne INT NOT NULL,
                                        panamera INT NOT NULL,
                                        taycan INT NOT NULL,
                                        trueno INT NOT NULL,
                                        supra INT NOT NULL,
                                        mark_II INT NOT NULL,
                                        crown INT NOT NULL,
                                        rx_7 INT NOT NULL,
                                        miata INT NOT NULL,
                                        roadster INT NOT NULL,
                                        rx_8 INT NOT NULL)'''
            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()
            zero = 0
            cursor = sqlite_connection.cursor()
            sqlite_insert_with_param = """INSERT INTO user
                                    (username, password, name, age, driving_experience, criminal, phone, email, card, 
                                    civic, nsx, s2000, prelude, stagea, skyline, silvia, GTR, p911, cayenne, panamera,
                                    taycan, trueno, supra, mark_II, crown, rx_7, miata, roadster, rx_8)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            data_tuple = (username, password, name, int(age), int(driving_experience), criminal, phone, email, card, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            print("data successfully inserted")
            sqlite_connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("ERROR", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

        self.root.destroy()
        enter = Enter()
        enter.run()

class Registration:
    def __init__(self):
        self.root = Tk()
        self.root.title('Авторизация')
        self.root.geometry('450x230+400+150')
        self.root.resizable=(False, False)

        self.main_label = Label(self.root, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
        self.username_label = Label(self.root, text='Имя пользователя', font=label_font , **base_padding)
        self.username_entry = Entry(self.root, bg='#fff', fg='#444', font=font_entry, highlightthickness=1, relief='solid')
        self.password_label = Label(self.root, text='Пароль', font=label_font , **base_padding)
        self.password_entry = Entry(self.root, bg='#fff', fg='#444', font=font_entry, show='*', highlightthickness=1, relief='solid')
        self.send_btn = Button(self.root, text='Зарегистрироваться', command=self.clicked, borderwidth=3, bg=color1, fg=color0)

    def clicked(self):
        output=open('logins.txt','+r')
        # логин и пароль
        username = self.username_entry.get()
        password = self.password_entry.get()

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
                        self.root.destroy()
                        self.run() 
            if (flag == 0):     
                s = (username+' '+password)
                output.write(s)
                output.close()
                self.root.destroy()
                data = Data()
                data.run()
                break
        

    def draw_widjets(self):
        self.main_label.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.send_btn.pack(**base_padding)
    
    def run(self):
        self.draw_widjets()
        self.root.mainloop()