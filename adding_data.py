import random
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class AddClientWindow:  # Клас для додавання нових клаєнтів

    def __init__(self, master, data_manager, back_callback):
        self.master = master
        self.master.title("Додати клієнта")
        # Визначення розмірів екрану
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Розрахунок координат для відображення вікна по центру екрану
        x = (screen_width - 200) // 2
        y = (screen_height - 300) // 2
        # Задаємо розміри та положення вікна
        self.master.geometry(f"200x340+{x}+{y}")

        self.data_manager = data_manager
        self.back_callback = back_callback

        self.create_widgets()

    def create_widgets(self):  # Метод для створення нового вікна для додавання даних клієнта
        # Створюємо елементи Label та Entry для відображення тексту та вводу даних
        tk.Label(self.master, text="Назва компанії:").pack(pady=5)
        self.company_name = tk.Entry(self.master)
        self.company_name.pack(pady=5)

        tk.Label(self.master, text="Им'я клієнта:").pack(pady=5)
        self.full_name = tk.Entry(self.master)
        self.full_name.pack(pady=5)

        tk.Label(self.master, text="Номер телефона (9 цифр):").pack(pady=5)
        self.phone_number = tk.Entry(self.master)
        self.phone_number.pack(pady=5)

        tk.Label(self.master, text="Тип послуги:").pack(pady=5)
        self.type_of_service = ttk.Combobox(self.master, values=["Кредит", "Купівля", "Аренда"])
        self.type_of_service.pack(pady=5)
        # Кнопка для зберігання даних
        ttk.Button(self.master, text="Зберегти", command=self.save_data).pack(pady=10)
        # Кнопка для закриття даного вікна
        ttk.Button(self.master, text="Назад", command=self.back_callback).pack(pady=10)

    def save_data(self):  # Метод для обробки даних
        # Зчитуємо дані з Entry та Combobox для подальшої перевіки та збереження в БД
        company_name = self.company_name.get()
        full_name = self.full_name.get()
        phone_number = self.phone_number.get()
        type_of_service = self.type_of_service.get()
        # Перевірка на путі поля
        if not company_name or not full_name or not phone_number or not type_of_service:
            tk.messagebox.showerror("Помилка", "Усі поля повинні бути заповнені.")
            return
        # Перевірка що номер телефону складається з 9 цифр
        if not phone_number.isdigit() or len(phone_number) != 9:
            tk.messagebox.showerror("Помилка", "Номер телефона повинен містити 9 цифр.")
            return
        # Перевірка що обрано тип посуги з допустимих
        if type_of_service not in ["Кредит", "Купівля", "Аренда"]:
            tk.messagebox.showerror("Помилка", "Обрано некоректний тип послуги.")
            return
        # Генерація  ID в  діапазоні від 100000 до 999999
        client_id = random.randint(100000, 999999)
        # Зберігаємо усі значення у список
        values = [client_id, company_name, full_name, phone_number, type_of_service]
        # Передаємо список з даними для збереження у відповіну таблицю БД
        self.data_manager.save_data("client", values)
        # Закриваємо дане вікно
        self.master.destroy()


class AddRealtorWindow:  # Клас для додавання нових рієлторів

    def __init__(self, master, data_manager, back_callback):
        self.master = master
        self.master.title("Додати ріелтора")
        # Визначення розмірів екрану
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Розрахунок координат для відображення вікна по центру екрану
        x = (screen_width - 200) // 2
        y = (screen_height - 300) // 2
        # Задаємо розміри та положення вікна
        self.master.geometry(f"200x340+{x}+{y}")

        self.data_manager = data_manager
        self.back_callback = back_callback

        self.create_widgets()

    def create_widgets(self):  # Метод для створення нового вікна для додавання даних рієлтора
        # Створюємо елементи Label та Entry для відображення тексту та вводу даних
        tk.Label(self.master, text="Назва компанії:").pack(pady=5)
        self.company_name = tk.Entry(self.master)
        self.company_name.pack(pady=5)

        tk.Label(self.master, text="Им'я ріелтора:").pack(pady=5)
        self.full_name = tk.Entry(self.master)
        self.full_name.pack(pady=5)

        tk.Label(self.master, text="Адреса:").pack(pady=5)
        self.address = tk.Entry(self.master)
        self.address.pack(pady=5)

        tk.Label(self.master, text="Номер телефона (9 цифр):").pack(pady=5)
        self.phone_number = tk.Entry(self.master)
        self.phone_number.pack(pady=5)
        # Кнопка для зберігання даних
        ttk.Button(self.master, text="Зберегти", command=self.save_data).pack(pady=10)
        # Кнопка для закриття даного вікна
        ttk.Button(self.master, text="Назад", command=self.back_callback).pack(pady=10)

    def save_data(self):  # Метод для обробки даних
        # Зчитуємо дані з Entry для подальшої перевіки та збереження в БД
        company_name = self.company_name.get()
        full_name = self.full_name.get()
        address = self.address.get()
        phone_number = self.phone_number.get()
        # Перевірка на пусті поля
        if not company_name or not full_name or not address or not phone_number:
            tk.messagebox.showerror("Помилка", "Усі поля повинні бути заповнені.")
            return
        # Перевірка що номер телефону складається з 9 цифр
        if not phone_number.isdigit() or len(phone_number) != 9:
            tk.messagebox.showerror("Помилка", "Номер телефона повинен містити 9 цифр.")
            return
        # Зберігаємо усі значення у список
        values = [company_name, full_name, address, phone_number]
        # Передаємо список з даними для збереження у відповіну таблицю БД
        self.data_manager.save_data("realtor", values)
        # Закриваємо дане вікно
        self.master.destroy()


class AddPropertyWindow:  # Клас для додавання нових нерухомостей

    def __init__(self, master, data_manager, back_callback):
        self.master = master
        self.master.title("Додати нерухомість")
        # Визначення розмірів екрану
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Розрахунок координат для відображення вікна по центру екрану
        x = (screen_width - 200) // 2
        y = (screen_height - 400) // 2
        # Задаємо розміри та положення вікна
        self.master.geometry(f"200x450+{x}+{y}")
        self.data_manager = data_manager
        self.back_callback = back_callback

        self.create_widgets()

    def create_widgets(self):  # Метод для створення нового вікна для додавання даних нерухомості
        # Створюємо елементи Label та Entry для відображення тексту та вводу даних
        tk.Label(self.master, text="Адреса:").pack(pady=5)
        self.address = tk.Entry(self.master)
        self.address.pack(pady=5)

        tk.Label(self.master, text="Площа (у кв. м):").pack(pady=5)
        self.square = tk.Entry(self.master)
        self.square.pack(pady=5)

        tk.Label(self.master, text="Поверх:").pack(pady=5)
        self.floor = tk.Entry(self.master)
        self.floor.pack(pady=5)

        tk.Label(self.master, text="Рік побудови:").pack(pady=5)
        self.year_of_construction = tk.Entry(self.master)
        self.year_of_construction.pack(pady=5)

        tk.Label(self.master, text="Кількість кімнат:").pack(pady=5)
        self.number_of_rooms = tk.Entry(self.master)
        self.number_of_rooms.pack(pady=5)

        tk.Label(self.master, text="Вартість:").pack(pady=5)
        self.price = tk.Entry(self.master)
        self.price.pack(pady=5)
        # Кнопка для зберігання даних
        ttk.Button(self.master, text="Зберегти", command=self.save_data).pack(pady=10)
        # Кнопка для закриття даного вікна
        ttk.Button(self.master, text="Назад", command=self.back_callback).pack(pady=10)

    def save_data(self):   # Метод для обробки даних
        # Зчитуємо дані з Entry для подальшої перевіки та збереження в БД
        address = self.address.get()
        square = self.square.get()
        floor = self.floor.get()
        year_of_construction = self.year_of_construction.get()
        number_of_rooms = self.number_of_rooms.get()
        price = self.price.get()
        # Перевірка на пусті рядки
        if not address or not square or not floor or not year_of_construction or not number_of_rooms or not price:
            tk.messagebox.showerror("Помилка", "Усі поля повинні бути заповнені.")
            return []
        # Перевірка що відповідні значення є числами
        try:
            square = float(square)
            floor = int(floor)
            year_of_construction = int(year_of_construction)
            number_of_rooms = int(number_of_rooms)
            price = int(price)
        except ValueError:
            tk.messagebox.showerror("Помилка",
                                    "Поля 'Площа', 'Поверх', 'Рік побудови', 'Кількість кімнат' та 'Вартість' повинні бути числами.")
            return
        # Перевірка що поверх не меньший за 1
        if floor < 1:
            tk.messagebox.showerror("Помилка", "Поверх не може бути меньшим 1.")
            return
        # Перевірка що рік побудови не меньший за  1980 та не більший за 2024 (Поточний рік)
        if year_of_construction > 2024 or year_of_construction < 1980:
            tk.messagebox.showerror("Помилка", "Рік побудови не може бути більшим 2024 та меньшим 1980.")
            return
        # Первірка що кількість кімнат не меньша за 1
        if number_of_rooms < 1:
            tk.messagebox.showerror("Помилка", "Кількість кімнат не може бути меншою 1.")
            return
        # Перевірка щою вартість не була меньшою за 1
        if price < 1:
            tk.messagebox.showerror("Помилка", "Вартість повинна бути більша 1.")
            return
        # Генерація ID в діапазоні від 100000 до 999999
        property_id = random.randint(100000, 999999)
        # Зберігаємо усі значення у список
        values = [property_id, address, square, floor, year_of_construction, number_of_rooms, price]
        # Передаємо список з даними для збереження у відповіну таблицю БД
        self.data_manager.save_data("real_estate", values)
        # Закриваємо дане вікно
        self.master.destroy()

