from tkinter import ttk
from tabulate import tabulate
import tkinter as tk


class ListWindow:  # відображення даних з БД

    def __init__(self, title, geometry, data, headers, master, data_manager, back_callback):
        self.data = data
        self.headers = headers
        self.master = master
        self.master.title(title)
        # Визначення розмірів екрану
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Розрахунок координат для відображення вікна по центру екрану
        x = (screen_width - geometry[0]) // 2  # Ширина окна: 600
        y = (screen_height - geometry[1]) // 2  # Высота окна: 400
        # Передавання координат для відображення вікна
        self.master.geometry(f"{geometry[0]}x{geometry[1]}+{x}+{y}")  # Задаем размеры и координаты окна

        self.data_manager = data_manager
        self.back_callback = back_callback

        self.create_widgets()

    def create_widgets(self):  # Метод для створення нового вікна з отриманими даними з БД
        # Створюємо вертикальну прокрутку
        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Створюємо текстове поле для отриманих даних
        self.text = tk.Text(self.master, wrap=tk.WORD, yscrollcommand=scrollbar.set, width=60)
        self.text.pack(expand=True, fill="both")
        # Задаємо спосід прокрутки
        scrollbar.config(command=self.text.yview)
        # Считуємо дані з відновідної таблиці
        data = self.data_manager.load_data(self.data)
        # Передаємо назви стовбців
        headers = self.headers
        # Відображаємо дані у текстовому полі з використанням tabulate
        table_str = tabulate(data, headers=headers, tablefmt="pretty")
        self.text.insert(tk.END, table_str)
        # Кнопка для закриття даного вікна
        ttk.Button(self.master, text="Назад", command=self.back_callback).pack(pady=10)
