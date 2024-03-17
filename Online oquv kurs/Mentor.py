from database_db import Database
import Class
import main

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

    1. Kurs qo'shish
    2. Kurs o'chirish
    0. Back 
        >>> """)
    if back == "1":
        name = input("Enter your name: ")
        description = input("Enter your description: ")
        rating = input("Enter your rating: ")
        active_students = input("Enter your active: ")
        mentor_id = input("Enter your mentor_id: ")
        language_id = input("Enter your language_id: ")
        price = input("Enter your price: ")
        courses_status_id = input("Enter your courses_status_id: ")
        print(Class.Student.insert_course(name, description, rating, active_students, mentor_id, language_id, price, courses_status_id))
        return courses(email, password)

    elif back == "2":
        tabl = "courses"
        column_name = input("Enter column name: ")
        data = input("Enter data: ")
        if column_name.lower() == "id":
            id = "courses_id"
            print(Class.Student.deleted_id(tabl, id, data))
            return courses(email, password)
        else:
            print(Class.Student.delete(tabl, column_name, data))
            return courses(email, password)

    elif back == "0":
        return mentor_panel(email, password)
    else:
        print("Invalid")
        return courses(email, password)




def mentor_panel(email, password):
    print("<< Mentor Panel >>")
    bolimlar = input("""
            1. Profil
            2. Cours
            0. Log Out
                >>> """)

    if bolimlar == "1":
        return Class.select_mentor(email, password)
    if bolimlar == "2":
        return courses(email, password)
    if bolimlar == "0":
        return main.main()
    else:
        print("Invalid")
        return mentor_panel(email, password)
