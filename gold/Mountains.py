import psycopg2

# Establishing the connection
# Устанавливаем соединение с базой данных PostgreSQL,
# используя указанные параметры, через модуль psycopg2.
conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='',
    host='127.0.0.1',
    port= '5432'
)
conn.autocommit = True
# Creating a cursor object using the cursor() method
# Создание объекта курсора с помощью метода cursor()
cursor = conn.cursor()

# Проверяем существование базы данных
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'mountains';")
exists = cursor.fetchone()

if not exists:
    # Создание базы данных в PostgreSQL
    cursor.execute("CREATE DATABASE mountains;")

    # Фиксируем транзакцию, чтобы изменения были сохранены.
    conn.commit()

conn = psycopg2.connect(
    database="mountains",
    user='postgres',
    password='',
    host='127.0.0.1',
    port= '5432'
)
cursor = conn.cursor()

# Проверяем существование таблицы
cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'my_mountain');")
table_exists = cursor.fetchone()[0]
if not table_exists:
    # Выполняется SQL-запрос для создания таблицы mountains.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_mountain (
            id SERIAL PRIMARY KEY,
    
            beauty_title VARCHAR(100),
            title VARCHAR(100) NOT NULL,
            other_titles VARCHAR(100),
            connect TEXT,
            add_time TIMESTAMP,
    
            user_email VARCHAR(100),
            user_phone VARCHAR(20),
            user_fam VARCHAR(100),
            user_name VARCHAR(100),
            user_otc VARCHAR(100),
    
            latitude VARCHAR(20),
            longitude VARCHAR(20),
            height VARCHAR(20),
    
            level_winter VARCHAR(10),
            level_summer VARCHAR(10),
            level_autumn VARCHAR(10),
            level_spring VARCHAR(10),
    
            images JSON
        );
    ''')
    # Фиксируем транзакцию, чтобы изменения были сохранены в базе данных.
    conn.commit()

# Closing the connection
conn.close()
