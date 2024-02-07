import sqlite3


class Data:  # Клас для роботи з БД

    def __init__(self, db_path="data.db"):
        # Подключаємось до БД
        self.db_path = db_path
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

    def create_tables(self):  # Метод для створення усіх необхідних таблиць в БД (Якщо вони не створені)
        # Створення таблиці зберігання даних рієлтора
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS realtor
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                            company_name TEXT, 
                            full_name TEXT,
                            address TEXT,
                            phone_number INTEGER
                            )
                        """)
        # Створення тадлиці зберігання даних клінта
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS client
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                            company_name TEXT, 
                            full_name TEXT,
                            phone_number INTEGER,
                            type_of_service TEXT)
                        """)
        # Створення таблиці зберігання даних нерухомості
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS real_estate
                            (address TEXT,
                            square INTEGER,
                            year_of_construction INTEGER,
                            number_of_rooms INTEGER,
                            price INTEGER,
                            property_identifier INTEGER)
                        """)
        self.con.commit()

    def request(self, request_text):  # Метод для викоання запитів до БД
        try:
            # Вирішуємо які дані буде отримано
            if request_text == "price" or request_text == "number_of_rooms":
                # Зчитуємо з відповідної таблиці БД дані
                self.cursor.execute(f"SELECT * FROM real_estate ORDER BY {request_text} DESC LIMIT 1")
                # Зберігаємо дані
                data = self.cursor.fetchall()
            elif request_text == "average":
                # Зчитуємо з відповідної таблиці БД дані про нерухомість з найбільшоб кількістю кімнат
                self.cursor.execute("SELECT AVG(price) FROM real_estate")
                # Зберігаємо дані
                data = self.cursor.fetchone()[0]
            return data
        except sqlite3.Error as e:
            print(f"Помилка при отримані даніх найдорожчої нерухомості: {e}")
            return []

    def load_data(self, table_name):  # Метод для зчитування усіх даних з відповідної таблиці
        try:
            # Зчитуємо усі дані з таблиці
            self.cursor.execute(f"SELECT * FROM {table_name}")
            # Зберігаємо дані
            data = self.cursor.fetchall()
            return data
        except sqlite3.Error as e:
            print(f"Помилка при зчитуванні даних з таблиці {table_name}: {e}")
            return []

    def save_data(self, table_name, values):  # Метод для запису нових даних до БД
        try:
            # Розділяємо дані зі списку комами для подальшого зберігання в БД
            placeholders = ",".join(["?" for x in values])
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(query, values)
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Помилка при зберіганні даних у таблицю {table_name}: {e}")

# git remote add origin https://github.com/Shark2ss/CourseWork