import sqlite3 as sl


def create_db():
    try:
        con = sl.connect('publ.db')
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


def create_table_users():
    try:
        con = sl.connect('publ.db')
        cur = con.cursor()
        create_que = """
        CREATE TABLE IF NOT EXISTS tUsers (
        id INTEGER PRIMARY KEY AUTOINNCREMENT, 
        userName TEXT NOT NULL,
        age INT NOT NULL,
        gender TEXT NOT NULL)"""
        cur.execute(create_que)
        cur.close()
        print('Table created')
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def create_table_publ():
    try:
        con = sl.connect('publ.db')
        cur = con.cursor()
        create_que = """
        CREATE TABLE IF NOT EXISTS tPubl (
        id INTEGER PRIMARY KEY AUTOINNCREMENT, 
        idUser FOREIGN KEY (tUsers) REFERENCES tUsers(id),
        title TEXT NOT NULL,
        description TEXT)"""
        cur.execute(create_que)
        cur.close()
        print('Table created')
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def create_table_comments():
    try:
        con = sl.connect('publ.db')
        cur = con.cursor()
        create_que = """
        CREATE TABLE IF NOT EXISTS tComments (
        id INTEGER PRIMARY KEY AUTOINNCREMENT, 
        textComm TEXT NOT NULL,
        idUser FOREIGN KEY (tUsers) REFERENCES tUsers(id),
        idPubl FOREIGN KEY (tPubl) REFERENCES tPubl(id))"""
        cur.execute(create_que)
        cur.close()
        print('Table created')
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def insert_data_us():
    try:
        con = sl.connect('publ.db')
        cursor = con.cursor()
        users = [("paninanq", 18, "женский"), ("arinaznchk", 19, "женский"), ("maria", 20, "женский"), ("vasya",20,"мужской"),
                 ("darya", 9, "женский")]
        insert_que = """
        INSERT INTO tUsers (userName, age, gender) VALUES ( ?, ?, ?')
        """
        cursor.executemany(insert_que, users)
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def insert_data_publ():
    try:
        con = sl.connect('publ.db')
        cursor = con.cursor()
        users = [(1, "love", "about_love"), (1, "sun", ". . ."), (3, "happy burthday", "party"), (5, "school", "study"),
                 (4, "university", "english")]
        insert_que = """
        INSERT INTO tPubl (id_user, title, description) VALUES ( ?, ?, ?')
        """
        cursor.executemany(insert_que, users)
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def insert_data_comm():
    try:
        con = sl.connect('publ.db')
        cursor = con.cursor()
        users = [(2, 1, "you're beautiful"), (3, 2, "cool"), (3, 1, "wow"), (1, 2, "thx"),
                 (4, 4, "congratulations")]
        insert_que = """
        INSERT INTO tComments (id_Users, id_Publ, textComm) VALUES ( ?, ?, ?')
        """
        cursor.executemany(insert_que, users)
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con:
            con.commit()
            con.close()


def select_data():
    try:
        con = sl.connect('publ.db')
        cur = con.cursor()
        select_query = "SELECT * FROM tUsers"
        cur.execute(select_query)
        res1 = cur.fetchall()
        # select_query = "SELECT * FROM tPubl"
        # cur.execute(select_query)
        # res2 = cur.fetchall()
        # select_query = "SELECT * FROM tComments"
        # cur.execute(select_query)
        # res3 = cur.fetchall()
        cur.close()
    except sl.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if con and res1:
            con.commit()
            con.close()
            return res1


def main():
    create_db()
    create_table_users()
    create_table_publ()
    create_table_comments()
    insert_data_us()
    insert_data_publ()
    insert_data_comm()
    select_data()


if __name__ == '__main__':
    main()