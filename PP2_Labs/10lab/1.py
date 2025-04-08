import psycopg2
import csv

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
  dbname="postgres",
  user="postgres",
  password="12345678",
  host="localhost",
  port="5432"
)
cur = conn.cursor()

# Создание таблицы
def create_table():
  cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
      id SERIAL PRIMARY KEY,
      first_name VARCHAR(100),
      phone_number VARCHAR(20)
    )
  """)
  conn.commit()

# Вставка данных вручную
def insert_user_input():
  name = input("Введите имя: ")
  phone = input("Введите номер телефона: ")
  cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
  conn.commit()
  print("Запись добавлена.")

# Загрузка из CSV
def insert_from_csv(file_path):
  with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if len(row) != 2:
        continue
      cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
  conn.commit()
  print("Данные из CSV добавлены.")

# Обновление данных
def update_data():
  name = input("Введите имя, которое нужно обновить: ")
  new_name = input("Новое имя (оставьте пустым, если не нужно менять): ")
  new_phone = input("Новый телефон (оставьте пустым, если не нужно менять): ")

  if new_name:
    cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, name))
  if new_phone:
    cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, new_name or name))
  conn.commit()
  print("Данные обновлены.")

# Фильтрация данных
def query_data():
  print("Фильтрация:")
  filter_type = input("Фильтр по (name/phone/all): ")
  if filter_type == "name":
    name = input("Введите имя: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
  elif filter_type == "phone":
    phone = input("Введите номер телефона: ")
    cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
  else:
    cur.execute("SELECT * FROM phonebook")
  rows = cur.fetchall()
  for row in rows:
    print(row)

# Удаление данных
def delete_data():
  field = input("Удалить по (name/phone): ")
  if field == "name":
    name = input("Введите имя: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
  elif field == "phone":
    phone = input("Введите номер: ")
    cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
  conn.commit()
  print("Данные удалены.")

# Меню
def menu():
  create_table()
  while True:
    print("\nМеню:")
    print("1 - Вставить пользователя вручную")
    print("2 - Загрузить из CSV")
    print("3 - Обновить данные")
    print("4 - Поиск")
    print("5 - Удаление")
    print("0 - Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
      insert_user_input()
    elif choice == "2":
      path = input("Введите путь к CSV файлу: ")
      insert_from_csv(path)
    elif choice == "3":
      update_data()
    elif choice == "4":
      query_data()
    elif choice == "5":
      delete_data()
    elif choice == "0":
      break
    else:
      print("Неверный выбор!")

  cur.close()
  conn.close()

if __name__ == "__main__":
  menu()