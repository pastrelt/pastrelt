import psycopg2
import json

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
    
            email VARCHAR(100),
            phone VARCHAR(20),
            fam VARCHAR(100),
            name VARCHAR(100),
            otc VARCHAR(100),
    
            latitude VARCHAR(20),
            longitude VARCHAR(20),
            height VARCHAR(20),
    
            winter VARCHAR(10),
            summer VARCHAR(10),
            autumn VARCHAR(10),
            spring VARCHAR(10),
    
            images JSON,
            
            status VARCHAR(10)
        );
    ''')
    # Фиксируем транзакцию, чтобы изменения были сохранены в базе данных.
    conn.commit()

# Closing the connection
conn.close()

# Класс для работы с базой данных
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="mountains",
            user='postgres',
            password='',
            host='127.0.0.1',
            port='5432'
        )
        self.cur = self.conn.cursor()

    def insert_pereval(self, pereval_data):
        # Метод insert_pereval принимает словарь pereval_data с информацией о перевале
        # и вставляет его в базу данных.
        # Статус модерации устанавливается в "new" при добавлении новой записи.
        query = '''
            INSERT INTO my_mountain (beauty_title, title, other_titles, connect, add_time,
                                     user_email, user_fam, user_name, user_otc, user_phone,
                                     latitude, longitude, height, level_winter, level_summer,
                                     level_autumn, level_spring, images, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        '''
        self.cur.execute(query, (pereval_data['beauty_title'], pereval_data['title'], pereval_data['other_titles'],
                                 pereval_data['connect'], pereval_data['add_time'], pereval_data['user']['email'],
                                 pereval_data['user']['fam'], pereval_data['user']['name'], pereval_data['user']['otc'],
                                 pereval_data['user']['phone'], pereval_data['coords']['latitude'],
                                 pereval_data['coords']['longitude'], pereval_data['coords']['height'],
                                 pereval_data['level']['winter'], pereval_data['level']['summer'],
                                 pereval_data['level']['autumn'], pereval_data['level']['spring'],
                                 psycopg2.extras.Json(pereval_data['images'], 'new' # начальный статус модерации
                                 )))
        inserted_id = self.cur.fetchone()[0]
        self.conn.commit()
        return inserted_id

    def update_status(self, pereval_id, new_status):
        # Mетод update_status принимает идентификатор перевала pereval_id и
        # новый статус new_status. Перед выполнением обновления проверяется,
        # что новый статус является одним из допустимых значений.
        # Затем выполняется SQL-запрос для обновления статуса записи в базе данных.
        valid_statuses = ['new', 'pending', 'accepted', 'rejected']
        if new_status not in valid_statuses:
            return {"status": 400, "message": "Недопустимое значение для статуса", "id": None}

        sql = """
        UPDATE pereval
        SET status = %s
        WHERE id = %s;
        """
        values = (new_status, pereval_id)

        try:
            self.cur.execute(sql, values)
            self.conn.commit()
            return {"status": 200, "message": "Статус успешно обновлен", "id": pereval_id}
        except psycopg2.Error as e:
            return {"status": 500, "message": str(e), "id": None}

