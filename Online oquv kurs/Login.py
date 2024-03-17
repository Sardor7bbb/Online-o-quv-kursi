from database_db import Database
from Students import student_panel
from Mentor import mentor_panel

import main


def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    query = f"SELECT first_name,email,password FROM students WHERE email = '{email}' AND password = '{password}'"
    query2 = f"SELECT first_name,email,password FROM mentor WHERE email = '{email}' AND password = '{password}' "

    natija = Database.connect(query, "select")

    natija2 = Database.connect(query2, "select")

    if len(natija or natija2) == 0:
        print("Email yoki password xato! ")
        return main.main()
    elif len(natija) != 0:
        print(f"<<<<<<<<<<<<<<<<< Salom {natija[0][0]} >>>>>>>>>>>>>>>>>>")
        return student_panel(email, password)
    elif len(natija2) != 0:
        print(f"<<<<<<<<<<<<<<<<< Salom {natija2[0][0]} >>>>>>>>>>>>>>>>>>")
        return mentor_panel(email, password)
    else:
        print("Invalid email or password")
