from database_db import Database
import Login


def register_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    password2 = input("Repeat your password: ")
    while password != password2:
        password = input("Enter your password: ")
        password2 = input("Repeat your password: ")
    bio = input("Enter your bio: ")
    contact_url = input("Enter your contact url: ")
    query = f"""INSERT INTO students (first_name, last_name, email, password, bio, contact_url) VALUES ('{first_name}', '{last_name}', '{email}', '{password}', '{bio}', '{contact_url}')"""
    Database.connect(query, "insert")
    print("Inserted into database")
    return Login.login()

