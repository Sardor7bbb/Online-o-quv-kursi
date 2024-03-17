import main
from Class import select_student
from database_db import Database


def courses(email, password):
    query = """SELECT courses.courses_id,mentor.first_name, mentor.last_name, courses.name,courses.rating,courses.active_students, language.name, courses_status.name,courses.price FROM courses
        INNER JOIN mentor
            ON mentor.mentor_id = courses.mentor_id
        INNER JOIN language
            ON language.language_id = courses.language_id
        INNER JOIN courses_status
            ON courses_status.courses_status_id = courses.courses_status_id;"""
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
                ID: {i[0]}
                Full Name: {i[1]} {i[2]}
                Name: {i[3]}
                Rating: {i[4]}
                Activ Students: {i[5]}
                Language: {i[6]}
                Status: {i[7]}
                Price: {i[8]}
            """)
    back = input("""

    1. Kurs sotib olish
    0. Back 
        >>> """)
    if back == "1":
        return buy(email, password)

    elif back == "0":
        return student_panel(email, password)
    else:
        print("Invalid")
        return courses(email, password)

def buy(email, password):
    kurs = input("Kurs id kiriting: ")
    query = f"""SELECT price FROM courses WHERE courses_id = {kurs}"""
    data = Database.connect(query, "select")
    narx = data[0][0]
    print(narx)


    query2 = f"SELECT * FROM students"
    data2 = Database.connect(query2, "select")
    for i in data2:
        if i[3] == email and i[4] == password:
            som = i[10]


    narxi = input(f"""
    Kursning narxi : {narx}$

    1. Sotib olish
    2. Bekor qilish
        >>> """)

    if narxi == "1":
        qiymat = som - narx
        print(qiymat)
        query = f"""UPDATE students SET balanc = '{qiymat}' WHERE email = '{email}'"""
        Database.connect(query, "update")
        print(f"""Xizmar muvofaqiyatli tugadi 

                Xozirgi balanc: {qiymat}$""")
        return balanc(email, password)

    elif narxi == "2":
        return student_panel(email, password)
    else:
        print("Invalid")
        return buy(email, password)

def balanc(email, password):
    query = """ SELECT * FROM students """
    data = Database.connect(query, "select")
    for i in data:
        if i[3] == email and i[4] == password:
            narxi = (f"""
            Your Balancing: {i[10]}""")
            print(narxi)
            buy = input("""
        1. Kurs sotib olish
        0. Back
            >>> """)

            if buy == "1":
                return courses(email, password)
            elif buy == "0":
                return student_panel(email, password)
            else:
                print("Invalid")
                return balanc(email, password)


def student_panel(email, password):
    print("<< Student Panel >>")
    headers = input("""
        1. Profil
        2. Cours
        3. Balanc
        0. Log Out
            >>> """)

    if headers == "1":
        return select_student(email, password)
    if headers == "2":
        return courses(email, password)
    if headers == "3":
        return balanc(email, password)
    if headers == "0":
        return main.main()
    else:
        print("Invalid")
        return student_panel(email, password)
