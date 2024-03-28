import sqlite3 as sl


def create_db():
    try:
        con = sl.connect('city.db')
        cursor = con.cursor()
        print('База данных создана и успешно подключена к SQLite')
        select_que = "select sqlite_version();"
        cursor.execute(select_que)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()
            print('Соединение с SQLite закрыто')


def create_table():
    try:
        con = sl.connect('city.db')
        cur = con.cursor()
        create_que = """
        CREATE TABLE IF NOT EXISTS tCity (
        number INTEGER PRIMARY KEY, 
        name TEXT NOT NULL )"""
        cur.execute(create_que)
        cur.close()
        print('Table created')
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def insert_data():
    try:
        con = sl.connect('city.db')
        cursor = con.cursor()
        values = ['St.Petersburg', 'Rostov-on-Don', 'Moscow', 'Kazan', 'Ryazan']
        for val in values:
            cursor.execute(f"INSERT INTO tCity (name) VALUES ('{val}')")
        cursor.close()
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()

def select_data():
    try:
        con = sl.connect('city.db')
        cur = con.cursor()
        select_query = "SELECT * FROM tCity"
        cur.execute(select_query)
        res = cur.fetchall()
        cur.close()
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con and res:
            con.commit()
            con.close()
            return res


def main():
    create_db()
    create_table()
    insert_data()
    print(select_data())


if __name__ == '__main__':
    main()