# библиотеки
from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from registration import Registration
from enter import Enter

# шрифты и отступы
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}
color0 = "#ffffff"
color1 = "#4456F0"


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Авторизация')
        self.root.geometry('450x230+400+150')
        self.root.resizable=(False, False)

        self.main_label = Label(self.root, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
        self.send_btn = Button(self.root, text='Вход', command=self.clicked_enter, width=15, borderwidth=3, bg=color1, fg=color0)
        self.send_btv = Button(self.root, text='Регистрация', command=self.clicked_reg, borderwidth=3, width=15, bg=color1, fg=color0)

    def clicked_enter(self):
        self.root.destroy()
        enter = Enter()
        enter.run()

    def clicked_reg(self):
        self.root.destroy()
        reg = Registration()
        reg.run()

    def draw_widjets(self):
        self.main_label.pack()
        self.send_btn.pack(**base_padding)
        self.send_btv.pack(**base_padding)


    def run(self):
        self.root.mainloop()


window = Window()
window.draw_widjets()
window.run()