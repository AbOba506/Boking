# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from main import Main

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class Enter:
    def __init__(self):
        self.root = Tk()
        self.root.title('Авторизация')
        self.root.geometry('450x230+400+150')
        self.root.resizable=(False, False)

        self.main_label = Label(self.root, text='Вход', font=font_header, justify=CENTER, **header_padding)
        self.username_label = Label(self.root, text='Имя пользователя', font=label_font , **base_padding)
        self.username_entry = Entry(self.root, bg='#fff', fg='#444', font=font_entry)
        self.password_label = Label(self.root, text='Пароль', font=label_font , **base_padding)
        self.password_entry = Entry(self.root, bg='#fff', fg='#444', font=font_entry, show='*')
        self.send_btn = Button(self.root, text='Войти', command=self.clicked)

    def clicked(self):
        output = open('logins.txt','+r')
        myusername = open('myusername.txt', '+r')
        username = self.username_entry.get()
        password = self.password_entry.get()
        s1 = 0
        s2 = 0
        while True:
            line =  output.readline()
            if not line:
                break
            username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card  = line.split() 
            if (username == username_in_file and password == password_in_file):
                self.root.destroy()
                s1 = 1
                main = Main()
                main.run()
                myusername.write(username + ' ' + password + ' ' + name + ' ' +  age + ' ' + driving_experience + ' ' + criminal + ' ' + phone + ' ' + email + ' ' + card + ' ')
            else:
                s2 = 0
        if (s1 == 0 and s2 ==0 ):
            messagebox.showerror('Ошибка','Неправильный логин или пароль')
        output.close()
        myusername.close()

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