import psycopg2
import csv

# Функция для подключения к базе данных
def connect():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="Pg_sql_2025_pp2",
        host="localhost",
        port="5432"
    )

# Загрузка данных из CSV-файла в таблицу phonebook
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    with open(r'C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab10\phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("Данные из CSV успешно добавлены.")
    cur.close()
    conn.close()

# Ввод данных вручную и добавление в таблицу
def insert_from_input():
    conn = connect()
    cur = conn.cursor()
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Данные успешно добавлены вручную.")
    cur.close()
    conn.close()

# Обновление имени или телефона в таблице phonebook
def update_data():
    conn = connect()
    cur = conn.cursor()
    print("Выберите, что хотите обновить:")
    print("1 — Обновить имя")
    print("2 — Обновить номер телефона")
    choice = input("Ваш выбор: ")

    if choice == "1":
        old_name = input("Введите старое имя: ")
        new_name = input("Введите новое имя: ")
        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
            (new_name, old_name)
        )
        print(f"Имя пользователя {old_name} обновлено на {new_name}.")
    
    elif choice == "2":
        name = input("Введите имя пользователя: ")
        new_phone = input("Введите новый номер телефона: ")
        cur.execute(
            "UPDATE phonebook SET phone_number = %s WHERE first_name = %s",
            (new_phone, name)
        )
        print(f"Номер телефона для {name} обновлен на {new_phone}.")
    
    else:
        print("Неверный выбор!")

    conn.commit()
    cur.close()
    conn.close()

# Функция для добавления нескольких пользователей с проверкой телефонов
def insert_multiple_users():
    conn = connect()
    cur = conn.cursor()

    # Пример списка пользователей и номеров телефонов
    users = ['John Doe', 'Jane Smith', 'Alice Johnson']
    phones = ['1234567890', '987654321', '5551234567']

    try:
        # Вызываем хранимую процедуру для вставки пользователей
        cur.execute("CALL insert_users_from_list(%s, %s)", (users, phones))
        conn.commit()
        print("Данные успешно добавлены или некорректные данные выведены.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        # Закрываем соединение с базой
        cur.close()
        conn.close()



# Поиск данных по имени или номеру (с фильтрами)
def query_data():
    conn = connect()
    cur = conn.cursor()
    print("Выберите фильтр для поиска:")
    print("1 — Показать всех пользователей")
    print("2 — Найти по имени")
    print("3 — Найти по номеру телефона")
    print("4 — Найти по части имени")

    choice = input("Ваш выбор: ")

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
        results = cur.fetchall()
    elif choice == "2":
        name = input("Введите имя для поиска: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
        results = cur.fetchall()
    elif choice == "3":
        phone = input("Введите номер телефона для поиска: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
        results = cur.fetchall()
    elif choice == "4":
        part = input("Введите часть имени: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + part + '%',))
        results = cur.fetchall()
    else:
        print("Неверный выбор!")
        return

    if results:
        print("Результаты поиска:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Ничего не найдено.")
    cur.close()
    conn.close()

# Удаление данных по имени или номеру телефона
def delete_data():
    conn = connect()
    cur = conn.cursor()
    print("Выберите способ удаления:")
    print("1 — Удалить по имени")
    print("2 — Удалить по номеру телефона")

    choice = input("Ваш выбор: ")
    if choice == "1":
        name = input("Введите имя пользователя для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        print(f"Пользователь(и) с именем '{name}' удалён(ы).")
    
    elif choice == "2":
        phone = input("Введите номер телефона для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
        print(f"Пользователь с номером '{phone}' удалён.")
    
    else:
        print("Неверный выбор!")

    conn.commit()
    cur.close()
    conn.close()

# Поиск по шаблону: имя, часть имени или номер (использует SQL-функцию search_by_pattern)
def search_by_pattern():
    pattern = input("Введите шаблон для поиска (например, часть имени или номера): ")

    conn = connect()
    cur = conn.cursor()

    # Вызов SQL-функции, определенной в базе
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    results = cur.fetchall()

    if results:
        print("Результаты поиска:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Ничего не найдено.")

    cur.close()
    conn.close()

# Функция для добавления нового пользователя или обновления номера, если имя уже существует
def insert_or_update_user():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")

    # Подключаемся к базе данных
    conn = connect()
    cur = conn.cursor()

    try:
        # Вызываем хранимую процедуру из базы данных
        cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
        conn.commit()
        print("Пользователь успешно добавлен или обновлён.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        # Закрываем соединение с базой
        cur.close()
        conn.close()

# Функция для добавления нескольких пользователей в таблицу phonebook
# Пользователь вводит имена и номера вручную
# Вызывает SQL-функцию insert_users_from_list, которая возвращает некорректные данные
def insert_multiple_users():
    conn = connect()
    cur = conn.cursor()

    # Запрос количества пользователей для ввода
    count = int(input("Сколько пользователей вы хотите добавить? "))

    # Инициализация списков для имён и номеров
    users = []
    phones = []

    # Цикл для сбора данных от пользователя
    for i in range(count):
        name = input(f"Введите имя пользователя #{i + 1}: ")
        phone = input(f"Введите номер телефона для {name}: ")
        users.append(name)
        phones.append(phone)

    try:
        # Вызов SQL-функции, которая добавляет пользователей и возвращает некорректные записи
        cur.execute(
            "SELECT * FROM insert_users_from_list(%s, %s);",
            (users, phones)
        )
        invalids = cur.fetchall()
        conn.commit()

        # Вывод некорректных данных, если они есть
        if invalids:
            print("Найдены некорректные данные:")
            for name, phone in invalids:
                print(f"Имя: {name}, Телефон: {phone}")
        else:
            print("Все пользователи успешно добавлены.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()

# Функция для получения данных с пагинацией (по limit и offset)
def query_data_with_pagination():
    conn = connect()
    cur = conn.cursor()
    
    # Ввод данных от пользователя с проверкой
    while True:
        try:
            print("Введите номер страницы для отображения (начиная с 1):")
            page = int(input())
            if page < 1:
                print("Номер страницы должен быть положительным числом.")
                continue
            break
        except ValueError:
            print("Введите корректный номер страницы.")

    while True:
        try:
            print("Введите количество записей на странице:")
            limit = int(input())
            if limit < 1:
                print("Количество записей на странице должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Введите корректное количество записей.")
    
    # Вычисляем смещение
    offset = (page - 1) * limit
    
    # Запрашиваем данные с пагинацией
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    results = cur.fetchall()
    
    if results:
        print(f"Результаты для страницы {page}:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Ничего не найдено.")
    
    cur.close()
    conn.close()

# Вызов функции для запроса данных с пагинацией
query_data_with_pagination()        

# Главное меню
print("Выберите действие:")
print("1 - Загрузить из CSV")
print("2 - Ввести вручную")
print("3 - Обновить данные")
print("4 - Найти данные")
print("5 - Удалить данные")
print("6 - Поиск по шаблону (из функции в БД)")
print("7 - Добавить/обновить пользователя")
print("8 - Массовое добавление пользователей с проверкой")

choice = input("Ваш выбор: ")

# Обработка выбора пользователя
if choice == "1":
    insert_from_csv()
elif choice == "2":
    insert_from_input()
elif choice == "3":
    update_data()
elif choice == "4":
    query_data()
elif choice == "5":

    delete_data()
elif choice == "6":
    search_by_pattern()
elif choice == "7":
    insert_or_update_user()
elif choice == "8":
    insert_multiple_users()
else:
    print("Неверный выбор!")
