import tkinter as tk
from tkinter import messagebox
from database import Data
import adding_data
from data_dasplay import ListWindow


class GUIApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Курсова робота")
        self.font = ("Times New Roman", 12)
        # Отримуємо розміри екрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Розчитуємо координати для центрування вікна
        x = (screen_width - 450) // 2
        y = (screen_height - 400) // 2
        # Задаємо розміри та положення вікна
        self.master.geometry(f"450x400+{x}+{y}")
        # Створюємо єкземляр класу Data
        self.data_manager = Data()

        self.create_widgets()

    def create_widgets(self):  # Метод для выдображення кнопок на вікні
        # Видаляємо кнопки при наявності
        for widget in self.master.winfo_children():
            widget.destroy()
        # Додаємо текстову мітку
        label = tk.Label(self.master, text="Ріелторська фірма", font=("Times New Roman", 15))
        label.pack(pady=20)
        # Додаємо кнопки 33-46
        button_clients = tk.Button(self.master, text="Список клієнтів", font=self.font, command=lambda: self.show_list("Список клієнтів"),
                                   width=20)
        button_clients.pack(pady=10)

        button_realtors = tk.Button(self.master, text="Список ріeлторів", font=self.font, command=lambda: self.show_list("Список рієлторів"),
                                    width=20)
        button_realtors.pack(pady=10)

        button_properties = tk.Button(self.master, text="Список нерухомостей", font=self.font,
                                      command=lambda: self.show_list("Список нерухомостей"), width=20)
        button_properties.pack(pady=10)

        button_data = tk.Button(self.master, text="Дані", font=self.font, command=self.show_data, width=20)
        button_data.pack(pady=10)

        tk.Button(self.master, text="Вихід", font=self.font, command=self.master.quit).pack(pady=10)

    def show_list(self, title):  # Метод для відображення відповідних даних з БД
        # Створюємо нове вікно для відображення відповідного списку
        list_window = tk.Toplevel(self.master)
        list_window.title(title)
        # Перевіряємо які дані будуть передаватися в майбутній єкземпляр класу
        if title == "Список клієнтів":
            # Задаємо назви стовпців для майбутнього єкземпляра класа
            headers = ["ID", "Компанія", "Им'я клієнта", "Номер телефона", "Тип послуги"]
            data = "client"
            # Задаємо розміри майбуьнього вікна
            geometry = [750, 430]
        elif title == "Список рієлторів":
            headers = ["Компанія", "Им'я", "Адреса", "Номер телефона"]
            geometry = [700, 430]
            data = "realtor"
        elif title == "Список нерухомостей":
            headers = ["Id", "Адреса", "Площа", "Поверх", "Рік побудови", "Кількість кімнат", "Вартість"]
            geometry = [800, 430]
            data = "real_estate"
        # Створюємо єкземпляр класу ListWindow з файлу data_display.py
        data_list = ListWindow(title, geometry, data, headers, list_window, self.data_manager, self.create_widgets)

    def show_data(self):  # Метод для створення нових відповідних кнопок на головному єкрані
        # Видаляємо старі кнопки
        for widget in self.master.winfo_children():
            widget.destroy()
        # додаємо нові кнопки
        tk.Button(self.master, text="Додати клієнта", font=self.font, command=lambda: self.add("Додати клієнта"), width=20).pack(pady=10)

        tk.Button(self.master, text="Додати рієлтора", font=self.font, command=lambda: self.add("Додати рієлтора"), width=20).pack(pady=10)

        tk.Button(self.master, text="Додати нерухомість", font=self.font, command=lambda: self.add("Додати нерухомість"), width=20).pack(pady=10)

        tk.Button(self.master, text="Найдорожча нарухомість", font=self.font, command=lambda: self.request("Найдорожча нерухомість"), width=20).pack(pady=10)

        tk.Button(self.master, text="Найбільша кількість\nкімнат", font=self.font, command=lambda: self.request("Найбільша кількість кімнат"), width=20).pack(pady=10)

        tk.Button(self.master, text="Средняя вартість", font=self.font, command=lambda: self.request("Середня вартість"), width=20).pack(pady=10)

        tk.Button(self.master, text="Назад", font=self.font, command=self.create_widgets).pack(pady=10)

    def request(self, request_name):  # Метод для виконанння відповідних запитів до БД
        # Вирішуємо який запит бде відправлено до БД
        if request_name == "Найбільша кількість кімнат":
            query_result = self.data_manager.request("number_of_rooms")
        elif request_name == "Найдорожча нерухомість":
            query_result = self.data_manager.request("price")
        elif request_name == "Середня вартість":
            query_result = f"Середня вартість нерухомості: {self.data_manager.request("average")}"
        # Відправляємо результати на відображення у відповідному методі
        self.show_result(request_name, query_result)

    def show_result(self, title, data):  # Метод для відображення результату запиту до БД
        # Перевіряємо тип отриманих результаті
        if isinstance(data, list):  # Якщо отримані дані список (Найдорожча нерухомість та Найбільша кількість кімнат)
            text = data[0]
            result = f"ID: {text[0]}\nАдреса: {text[1]}\nПлоща: {text[2]}\nПоверх: {text[3]}\nРік побудови: {text[4]}\nКількість кімнат: {text[5]}\nВартість: {text[6]}"
            messagebox.showinfo(title, result)
        elif isinstance(data, str):  # Якщо результат рядок (Середня вартість)
            messagebox.showinfo(title, data)
        else:  # У випадку якщо дані пусті або не відповідний тип резутатів
            messagebox.showinfo(title, "Дані відстні.")

    def add(self, title):  # Метод для запису відповідних даних до БД
        # Створюємо нове вікно
        add_data_window = tk.Toplevel(self.master)
        add_data_window.title(title)
        # Перевіряємо передані дані та вирішуємо яке вікно буде створенно
        if title == "Додати клієнта":
            add_client = adding_data.AddClientWindow(add_data_window, self.data_manager, self.create_widgets)
        elif title == "Додати рієлтора":
            add_realtor = adding_data.AddRealtorWindow(add_data_window, self.data_manager, self.create_widgets)
        elif title == "Додати нерухомість":
            add_property = adding_data.AddPropertyWindow(add_data_window, self.data_manager, self.create_widgets)


if __name__ == "__main__":
    Data().create_tables()
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
