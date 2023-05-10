# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3 as sql

# При необходимости (Удаление таблицы Students):
# cur.execute('DROP TABLE IF EXISTS Students')

with sql.connect('teatchers.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Students (
        Student_Id  INTEGER,
        Student_Name  TEXT,
        School_Id  INTEGER PRIMARY KEY
        )""")


    # cur.execute(""" INSERT INTO Students VALUES(201, 'Иван', 1)""")
    # cur.execute(""" INSERT INTO Students VALUES(202, 'Петр', 2)""")
    # cur.execute(""" INSERT INTO Students VALUES(203, 'Анастасия', 3)""")
    # cur.execute(""" INSERT INTO Students VALUES(204, 'Игорь', 4)""")

    # cur.execute("""SELECT * FROM Students""")
    # result = cur.fetchall()
    # print(result)

    def find_students(value):
        cur.execute(f"""
        SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name  FROM Students, School 
        WHERE Students.Student_Id == {value} AND Students.School_Id == School.School_Id""")
        result = cur.fetchall()

        print(f"""
    ID Студента: {result[0][0]}
    Имя студента: {result[0][1]}
    ID школы: {result[0][2]}
    Название школы: {result[0][3]}
    """)

    find_students(input('Введите ID студента '))