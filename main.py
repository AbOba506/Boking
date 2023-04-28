# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from PIL import Image, ImageTk

# шрифты и отступы
font_header = ('Arial', 15)
font_text = ('Arial', 10)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Система Бронирования')
        self.root.geometry('450x230+400+150')
        self.root.resizable=(False, False)
        self.photo = tk.PhotoImage(file='photo.png')
        self.root.iconphoto(False, self.photo)

        self.bron_label = Label(self.root, text='Бронирование', font=('Arial', 15, 'bold'), justify=CENTER, **header_padding)
        self.btn1 = tk.Button(self.root, text='Главная', command=self.main_page, font=('Arial', 15, 'bold'), borderwidth=5, width=15)
        self.btn2 = tk.Button(self.root, text='Личный кабинет', command=self.lk, font=('Arial', 15, 'bold'), borderwidth=5, width=15)
        self.btn3 = tk.Button(self.root, text='Ассортимент', command=self.def_assortiment,font=('Arial', 15, 'bold'), borderwidth=5, width=15)

    def draw_widjets(self):
        self.bron_label.grid(row=0, column=1)
        self.btn1.grid(row=1, column=0)
        self.btn2.grid(row=2, column=0)
        self.btn3.grid(row=3, column=0)
    
    def run(self):
        self.draw_widjets()
        self.root.mainloop()
    
    # Функция перехода в главную страницу
    def main_page(self):
        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_main():
            window_main_page.destroy()
            main = Main()
            main.run()
        # главное окно приложения
        window_main_page = Tk()
        # заголовок окна
        window_main_page.title('Главная')
        # размер окна
        window_main_page.geometry('900x400+300+150')
        # менять размер
        window_main_page.resizable(False, False)

        # настройка
        lk_label = Label(window_main_page, text='Главная страница', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=0, column=1)
        lk_label = Label(window_main_page, text='Добро пожаловать в наше приложение для броинрования автомобилей!', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=1, column=1)
        lk_label = Label(window_main_page, text='В нашем приложении вы можете забронировать такие машины как:', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=2, column=1)
        lk_label = Label(window_main_page, text='Honda Civic, Porshe 911, Nissan Skyline, Toyota Supra, Toyota Trueno', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=3, column=1)
        exit_main_menu = Button(window_main_page, text='Выйти', command=exit_main, borderwidth=5, width=10)
        exit_main_menu.grid(row=0, column=2)

        window_main_page.grid_columnconfigure(0, minsize=100)
        window_main_page.grid_columnconfigure(1, minsize=250)
        # главный цикл
        window_main_page.mainloop()
    
    # Функция перехода в лк
    def lk(self):
        # Отдельное окно оплаты
        def pay_def():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pay():
                window_pay.destroy()
                main = Main()
                main.run()
            # главное окно приложения
            window_pay = Tk()
            # заголовок окна
            window_pay.title('Оплата')
            # размер окна
            window_pay.geometry('450x230+400+150')
            # менять размер
            window_pay.resizable(False, False)

            myusername = open('myusername.txt', '+r')
            header_padding_1 = {'padx': 10, 'pady': 7}
            line = myusername.readline()
            username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card = line.split()

            # настройка
            pay_label = Label(window_pay, text='Оплата', font=font_header, justify=CENTER, **header_padding)
            pay_label.grid(row=0, column=1)

            # метка номер карты
            card_label = Label(window_pay, text='Номер карты', font=('Arial', 12), **header_padding_1)
            card_label.grid(row=1, column=0)
            # номер карты
            card_entry = Label(window_pay, text=card, font=('Arial', 12), **header_padding_1)
            card_entry.grid(row=1, column=1)

            pay_button_out = Button(window_pay, text='Выйти', command=exit_pay, borderwidth=5, width=10)
            pay_button_out.grid(row=0, column=2)

            window_pay.grid_columnconfigure(0, minsize=80)
            window_pay.grid_columnconfigure(1, minsize=200)


            # главный цикл
            window_pay.mainloop()

        # Отдельное окно Контактные данные
        def contact_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_cd():
                window_cd.destroy()
                main = Main()
                main.run()
            # главное окно приложения
            window_cd = Tk()
            # заголовок окна
            window_cd.title('Контактные данные')
            # размер окна
            window_cd.geometry('450x230+400+150')
            # менять размер
            window_cd.resizable(False, False)
            myusername = open('myusername.txt', '+r')
            header_padding_1 = {'padx': 10, 'pady': 7}

            line = myusername.readline()
            username_in_file, password_in_file, name, age, driving_experience, criminal, phone, email, card = line.split() 

            # настройка
            cd_label = Label(window_cd, text='Контактные данные', font=font_header, justify=CENTER, **header_padding)
            cd_label.grid(row=0, column=1)
            cd_button_out = Button(window_cd, text='Выйти', command=exit_cd, borderwidth=5, width=10)
            cd_button_out.grid(row=0, column=2)

            # метка номер телефона
            phone_label = Label(window_cd, text='Номер телефона', font=('Arial', 12), **header_padding_1)
            phone_label.grid(row=1, column=0)

            # номер телефона
            phone_entry = Label(window_cd, text=phone, font=('Arial', 12), **header_padding_1)
            phone_entry.grid(row=1, column=1)

            # метка E-mail
            email_label = Label(window_cd, text='E-mail', font=('Arial', 12), **header_padding_1)
            email_label.grid(row=2, column=0)

            # E-mail
            email_entry = Label(window_cd, text=email, font=('Arial', 12), **header_padding_1)
            email_entry.grid(row=2, column=1)

            window_cd.grid_columnconfigure(0, minsize=80)
            window_cd.grid_columnconfigure(1, minsize=200)

            # главный цикл
            window_cd.mainloop()

        # Отдельное окно Личные данные
        def personal_data():
            window_lk.destroy()
            # функция выхода на домашнюю страницу
            def exit_pd():
                window_pd.destroy()
                main = Main()
                main.run()

            # главное окно приложения
            window_pd = Tk()
            # заголовок окна
            window_pd.title('Личные данные')
            # размер окна
            window_pd.geometry('450x330+400+150')
            # менять размер
            window_pd.resizable(False, False)
            myusername = open('myusername.txt', '+r')
            # настройка
            pd_label = Label(window_pd, text='Личные данные', font=font_header, justify=CENTER, **header_padding)
            pd_label.grid(row=0, column=1)
            # Имя
            pd_label1 = Label(window_pd, text='Имя', font=font_text, **header_padding)
            pd_label1.grid(row=1, column=0)
            login, password, name, age, driving_experience, criminal, phone, email, card = myusername.readline().split()
            pd_label7 = Label(window_pd, text=name, font=font_text, **header_padding)
            pd_label7.grid(row=1, column=1)
            # Логин
            pd_label2 = Label(window_pd, text='Логин', font=font_text, **header_padding)
            pd_label2.grid(row=2, column=0)
            pd_label8 = Label(window_pd, text=login, font=font_text, **header_padding)
            pd_label8.grid(row=2, column=1)
            # Пароль
            pd_label3 = Label(window_pd, text='Пароль', font=font_text, justify=CENTER, **header_padding)
            pd_label3.grid(row=3, column=0)
            pd_label9 = Label(window_pd, text=password, font=font_text, **header_padding)
            pd_label9.grid(row=3, column=1)
            # Возраст
            pd_label4 = Label(window_pd, text='Возраст', font=font_text, justify=CENTER, **header_padding)
            pd_label4.grid(row=4, column=0)
            pd_label9 = Label(window_pd, text=age, font=font_text, **header_padding)
            pd_label9.grid(row=4, column=1)
            # Опыт вождения
            pd_label5 = Label(window_pd, text='Опыт вождения', font=font_text, justify=CENTER, **header_padding)
            pd_label5.grid(row=5, column=0)
            pd_label10 = Label(window_pd, text=driving_experience, font=font_text, **header_padding)
            pd_label10.grid(row=5, column=1)
            # судимость
            pd_label6 = Label(window_pd, text='Cудимость', font=font_text, justify=CENTER, **header_padding)
            pd_label6.grid(row=6, column=0)
            pd_label9 = Label(window_pd, text=criminal, font=font_text, **header_padding)
            pd_label9.grid(row=6, column=1)
            # Выйти
            pd_button_out = Button(window_pd, text='Выйти', command=exit_pd, borderwidth=5, width=10)
            pd_button_out.grid(row=0, column=2)
            window_pd.grid_rowconfigure(0, minsize=4)
            window_pd.grid_rowconfigure(1, minsize=4)
            window_pd.grid_columnconfigure(0, minsize=90)
            window_pd.grid_columnconfigure(1, minsize=220)
            myusername.close()
            # главный цикл
            window_pd.mainloop()

        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_lk():
            window_lk.destroy()
            main = Main()
            main.run()
        # главное окно приложения
        window_lk = Tk()
        # заголовок окна
        window_lk.title('Личный кабинет')
        # размер окна
        window_lk.geometry('450x230+400+150')
        # менять размер
        window_lk.resizable(False, False)

        # настройка
        lk_label = Label(window_lk, text='Личный кабинет', font=font_header, justify=CENTER, **header_padding)
        lk_label.grid(row=0, column=1)
        pd_button_out = Button(window_lk, text='Выйти', command=exit_lk, borderwidth=5, width=10)
        pd_button_out.grid(row=0, column=2)
        window_lk.grid_columnconfigure(0, minsize=70)
        window_lk.grid_columnconfigure(1, minsize=220)

        # кнопка Личные данные
        pers_data = Button(window_lk, text='Личные данные', command=personal_data, borderwidth=5, width=15)
        pers_data.grid(row=1, column=0)

        # кнопка Контактные данные
        cont_data= Button(window_lk, text='Контактные данные', command=contact_data, borderwidth=5, width=15)
        cont_data.grid(row=2, column=0)

        # кнопка Оплата
        pay = Button(window_lk, text='Оплата', command=pay_def, borderwidth=5, width=15)
        pay.grid(row=3, column=0)

        window_lk.grid_rowconfigure(2, minsize=60)

        # главный цикл
        window_lk.mainloop()
    
    # Функция перехода в Ассортимент
    def def_assortiment(self):
        self.root.destroy()
        # функция выхода на домашнюю страницу
        def exit_asortiment():
            window_assortiment.destroy()
            main = Main()
            main.run()
        # главное окно приложения
        window_assortiment = Tk()
        # заголовок окна
        window_assortiment.title('Ассортимент')
        # размер окна
        window_assortiment.geometry('450x230+400+150')
        # менять размер
        window_assortiment.resizable(False, False)

        # настройка
        lk_label = Label(window_assortiment, text='Ассортимент', font=font_header, justify=CENTER, **header_padding)
        lk_label.place(x = 150, y = 10)

        exit_main_menu = Button(window_assortiment, text='Выйти', command=exit_asortiment, borderwidth=5, width=10)
        exit_main_menu.place(x = 335, y = 20)
        
        # Функция перехода на страницу Civic
        def civic():
            window_assortiment.destroy()
            def exit_civic():
                window_civic.destroy()
                main = Main()
                main.run()
            window_civic = Tk()
            window_civic.title('Honda Civic')
            window_civic.geometry('900x650+300+20')
            window_civic.resizable(False, False)
            # настройка
            honda_civic_label = Label(window_civic, text='Honda Civic', font=('Arial',20), justify=CENTER, **header_padding)
            honda_civic_label.place(x = 390, y = 10)
            exit_honda_civic = Button(window_civic, text='Выйти', command=exit_civic, borderwidth=5,font=('Arial',16), width=10)
            exit_honda_civic.place(x = 750, y = 20)
            civic_photo = Image.open("data\\civic.png")
            civic_photo = civic_photo.resize((440, 350), Image.ANTIALIAS)
            civic_photo = ImageTk.PhotoImage(civic_photo)
            civic_label = Label(image = civic_photo, borderwidth=0)
            civic_label.image = civic_photo
            civic_label.place(x = 240, y = 70)
            honda_civic_label = Label(window_civic, text='Производитель: Honda', font=font_header, justify=CENTER)
            honda_civic_label.place(x = 240, y = 420)
            honda_civic_label = Label(window_civic, text='Модель: Civic type R', font=font_header, justify=CENTER)
            honda_civic_label.place(x = 240, y = 450)
            honda_civic_label = Label(window_civic, text='Тип кузова: 5-и дверная', font=font_header, justify=CENTER)
            honda_civic_label.place(x = 240, y = 480)
            honda_civic_label = Label(window_civic, text='Компоновка: переднеприводная', font=font_header, justify=CENTER)
            honda_civic_label.place(x = 240, y = 510)
            honda_civic_label = Label(window_civic, text='Стоимость за час: 2000 рублей', font=font_header, justify=CENTER)
            honda_civic_label.place(x = 240, y = 540)
            def book_civic():
                messagebox.showinfo('Информация','Вы успешно забронировали машину Honda Civic')
            book_honda_civic = Button(window_civic, text='Забронировать', command=book_civic, borderwidth=5, width=20, height=1, font=('Arial',16))
            book_honda_civic.place(x = 350, y = 570)
            # главный цикл
            window_civic.mainloop()
        
        # Фото Honda civic
        civic_photo = Image.open("data\\civic.png")
        civic_photo = civic_photo.resize((80, 70), Image.ANTIALIAS)
        civic_photo = ImageTk.PhotoImage(civic_photo)
        civic_label = Button(image = civic_photo, borderwidth=0, command=civic)
        civic_label.image = civic_photo
        civic_label.place(x = 5, y = 70)

        civic_name = Label(window_assortiment, text='Honda Civic', font=('Arial',10), justify=CENTER, width=10)
        civic_name.place(x=5, y=140)
        
        # Функция перехода на страницу Porshe
        def porshe():
            window_assortiment.destroy()
            def exit_porshe():
                window_porshe.destroy()
                main = Main()
                main.run()
            window_porshe = Tk()
            window_porshe.title('Porshe 911')
            window_porshe.geometry('900x650+300+20')
            window_porshe.resizable(False, False)
            # настройка
            porshe_label = Label(window_porshe, text='Porshe 911', font=('Arial',20), justify=CENTER, **header_padding)
            porshe_label.place(x = 390, y = 10)
            exit_porshe = Button(window_porshe, text='Выйти', command=exit_porshe, borderwidth=5,font=('Arial',16), width=10)
            exit_porshe.place(x = 750, y = 20)
            porshe_photo = Image.open("data\\porshe.png")
            porshe_photo = porshe_photo.resize((440, 350), Image.ANTIALIAS)
            porshe_photo = ImageTk.PhotoImage(porshe_photo)
            porshe_label = Label(image = porshe_photo, borderwidth=0)
            porshe_label.image = porshe_photo
            porshe_label.place(x = 240, y = 70)
            porshe_label = Label(window_porshe, text='Производитель: Porshe', font=font_header, justify=CENTER)
            porshe_label.place(x = 240, y = 420)
            porshe_label = Label(window_porshe, text='Модель: 911', font=font_header, justify=CENTER)
            porshe_label.place(x = 240, y = 450)
            porshe_label = Label(window_porshe, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
            porshe_label.place(x = 240, y = 480)
            porshe_label = Label(window_porshe, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
            porshe_label.place(x = 240, y = 510)
            porshe_label = Label(window_porshe, text='Стоимость за час: 5000 рублей', font=font_header, justify=CENTER)
            porshe_label.place(x = 240, y = 540)
            def book_porshe():
                messagebox.showinfo('Информация','Вы успешно забронировали машину Porshe 911')
            book_porshe = Button(window_porshe, text='Забронировать', command=book_porshe, borderwidth=5, width=20, height=1, font=('Arial',16))
            book_porshe.place(x = 350, y = 570)
            # главный цикл
            window_porshe.mainloop()
        
        # Фото Porshe
        porshe_photo = Image.open("data\\porshe.png")
        porshe_photo = porshe_photo.resize((80, 70), Image.ANTIALIAS)
        porshe_photo = ImageTk.PhotoImage(porshe_photo)
        porshe_label = Button(image = porshe_photo, borderwidth=0, command=porshe)
        porshe_label.image = porshe_photo
        porshe_label.place(x = 95, y = 70)

        porshe_name = Label(window_assortiment, text='Porshe 911', font=('Arial',10), justify=CENTER, width=10)
        porshe_name.place(x=90, y=140)

        # Функция перехода на страницу Skyline
        def skyline():
            window_assortiment.destroy()
            def exit_skyline():
                window_skyline.destroy()
                main = Main()
                main.run()
            window_skyline = Tk()
            window_skyline.title('Nissan Skyline')
            window_skyline.geometry('900x650+300+20')
            window_skyline.resizable(False, False)
            # настройка
            skyline_label = Label(window_skyline, text='Nissan Skyline', font=('Arial',20), justify=CENTER, **header_padding)
            skyline_label.place(x = 390, y = 10)
            exit_skyline = Button(window_skyline, text='Выйти', command=exit_skyline, borderwidth=5,font=('Arial',16), width=10)
            exit_skyline.place(x = 750, y = 20)
            skyline_photo = Image.open("data\\skyline.png")
            skyline_photo = skyline_photo.resize((440, 350), Image.ANTIALIAS)
            skyline_photo = ImageTk.PhotoImage(skyline_photo)
            skyline_label = Label(image = skyline_photo, borderwidth=0)
            skyline_label.image = skyline_photo
            skyline_label.place(x = 240, y = 70)
            skyline_label = Label(window_skyline, text='Производитель: Nissan', font=font_header, justify=CENTER)
            skyline_label.place(x = 240, y = 420)
            skyline_label = Label(window_skyline, text='Модель: Skyline GT-R R34', font=font_header, justify=CENTER)
            skyline_label.place(x = 240, y = 450)
            skyline_label = Label(window_skyline, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
            skyline_label.place(x = 240, y = 480)
            skyline_label = Label(window_skyline, text='Компоновка: полноприводная', font=font_header, justify=CENTER)
            skyline_label.place(x = 240, y = 510)
            skyline_label = Label(window_skyline, text='Стоимость за час: 6000 рублей', font=font_header, justify=CENTER)
            skyline_label.place(x = 240, y = 540)
            def book_skyline():
                messagebox.showinfo('Информация','Вы успешно забронировали машину Nissan Skyline')
            book_skyline = Button(window_skyline, text='Забронировать', command=book_skyline, borderwidth=5, width=20, height=1, font=('Arial',16))
            book_skyline.place(x = 350, y = 570)
            # главный цикл
            window_skyline.mainloop()

        # Фото Skyline
        skyline_photo = Image.open("data\\skyline.png")
        skyline_photo = skyline_photo.resize((80, 70), Image.ANTIALIAS)
        skyline_photo = ImageTk.PhotoImage(skyline_photo)
        skyline_label = Button(image = skyline_photo, borderwidth=0, command=skyline)
        skyline_label.image = skyline_photo
        skyline_label.place(x = 180, y = 70)

        skyline_name = Label(window_assortiment, text='Nissan Skyline', font=('Arial',10), justify=CENTER, width=10)
        skyline_name.place(x=178, y=140)

        # Функция перехода на страницу Supra
        def supra():
            window_assortiment.destroy()
            def exit_supra():
                window_supra.destroy()
                main = Main()
                main.run()
            window_supra = Tk()
            window_supra.title('Toyota Supra')
            window_supra.geometry('900x650+300+20')
            window_supra.resizable(False, False)
            # настройка
            supra_label = Label(window_supra, text='Toyota Supra', font=('Arial',20), justify=CENTER, **header_padding)
            supra_label.place(x = 390, y = 10)
            exit_supra = Button(window_supra, text='Выйти', command=exit_supra, borderwidth=5,font=('Arial',16), width=10)
            exit_supra.place(x = 750, y = 20)
            supra_photo = Image.open("data\\supra.png")
            supra_photo = supra_photo.resize((440, 350), Image.ANTIALIAS)
            supra_photo = ImageTk.PhotoImage(supra_photo)
            supra_label = Label(image = supra_photo, borderwidth=0)
            supra_label.image = supra_photo
            supra_label.place(x = 240, y = 70)
            supra_label = Label(window_supra, text='Производитель: Toyota', font=font_header, justify=CENTER)
            supra_label.place(x = 240, y = 420)
            supra_label = Label(window_supra, text='Модель: Supra A80', font=font_header, justify=CENTER)
            supra_label.place(x = 240, y = 450)
            supra_label = Label(window_supra, text='Тип кузова: 2-x дверная', font=font_header, justify=CENTER)
            supra_label.place(x = 240, y = 480)
            supra_label = Label(window_supra, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
            supra_label.place(x = 240, y = 510)
            supra_label = Label(window_supra, text='Стоимость за час: 4000 рублей', font=font_header, justify=CENTER)
            supra_label.place(x = 240, y = 540)
            def book_supra():
                messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Supra')
            book_supra = Button(window_supra, text='Забронировать', command=book_supra, borderwidth=5, width=20, height=1, font=('Arial',16))
            book_supra.place(x = 350, y = 570)
            # главный цикл
            window_supra.mainloop()

        # Фото Supra
        supra_photo = Image.open("data\\supra.png")
        supra_photo = supra_photo.resize((80, 70), Image.ANTIALIAS)
        supra_photo = ImageTk.PhotoImage(supra_photo)
        supra_label = Button(image = supra_photo, borderwidth=0, command=supra)
        supra_label.image = supra_photo
        supra_label.place(x = 270, y = 70)

        supra_name = Label(window_assortiment, text='Toyota Supra', font=('Arial',10), justify=CENTER, width=10)
        supra_name.place(x=270, y=140)

        # Функция перехода на страницу Supra
        def trueno():
            window_assortiment.destroy()
            def exit_trueno():
                window_trueno.destroy()
                main = Main()
                main.run()
            window_trueno = Tk()
            window_trueno.title('Toyota Trueno')
            window_trueno.geometry('900x650+300+20')
            window_trueno.resizable(False, False)
            # настройка
            trueno_label = Label(window_trueno, text='Toyota Trueno', font=('Arial',20), justify=CENTER, **header_padding)
            trueno_label.place(x = 390, y = 10)
            exit_trueno = Button(window_trueno, text='Выйти', command=exit_trueno, borderwidth=5,font=('Arial',16), width=10)
            exit_trueno.place(x = 750, y = 20)
            trueno_photo = Image.open("data\\trueno.png")
            trueno_photo = trueno_photo.resize((440, 350), Image.ANTIALIAS)
            trueno_photo = ImageTk.PhotoImage(trueno_photo)
            trueno_label = Label(image = trueno_photo, borderwidth=0)
            trueno_label.image = trueno_photo
            trueno_label.place(x = 240, y = 70)
            trueno_label = Label(window_trueno, text='Производитель: Toyota', font=font_header, justify=CENTER)
            trueno_label.place(x = 240, y = 420)
            trueno_label = Label(window_trueno, text='Модель: Trueno AE86', font=font_header, justify=CENTER)
            trueno_label.place(x = 240, y = 450)
            trueno_label = Label(window_trueno, text='Тип кузова: 3-x дверная', font=font_header, justify=CENTER)
            trueno_label.place(x = 240, y = 480)
            trueno_label = Label(window_trueno, text='Компоновка: заднеприводная', font=font_header, justify=CENTER)
            trueno_label.place(x = 240, y = 510)
            trueno_label = Label(window_trueno, text='Стоимость за час: 3000 рублей', font=font_header, justify=CENTER)
            trueno_label.place(x = 240, y = 540)
            def book_trueno():
                messagebox.showinfo('Информация','Вы успешно забронировали машину Toyota Trueno')
            book_trueno = Button(window_trueno, text='Забронировать', command=book_trueno, borderwidth=5, width=20, height=1, font=('Arial',16))
            book_trueno.place(x = 350, y = 570)
            # главный цикл
            window_trueno.mainloop()

        # Фото Trueno
        trueno_photo = Image.open("data\\trueno.png")
        trueno_photo = trueno_photo.resize((80, 70), Image.ANTIALIAS)
        trueno_photo = ImageTk.PhotoImage(trueno_photo)
        trueno_label = Button(image = trueno_photo, borderwidth=0, command=trueno)
        trueno_label.image = trueno_photo
        trueno_label.place(x = 360, y = 70)

        trueno_name = Label(window_assortiment, text='Toyota Trueno', font=('Arial',10), justify=CENTER, width=10)
        trueno_name.place(x=360, y=140)
        
        # главный цикл
        window_assortiment.mainloop()