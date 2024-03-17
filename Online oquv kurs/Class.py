from database_db import Database
import Students
import Mentor


class Student:





    @staticmethod
    def select(tabl):
        query =f"""SELECT * FROM {tabl}"""
        Database.connect(query, "select")


    @staticmethod
    def insert(first_name, last_name, email, password, bio, contact_url):
        query = f"""INSERT INTO student(first_name,last_name,email,password,bio,contact_url) VALUES ('{first_name}','{last_name}','{email}','{password}','{bio}','{contact_url}')"""
        Database.connect(query, "insert")


    @staticmethod
    def insert_course(name, description, rating, active_students, mentor_id, language_id, price, courses_status_id):
        query = f"""INSERT INTO courses(name,description,rating,active_students,mentor_id,language_id,price,courses_status_id) VALUES ('{name}','{description}','{rating}','{active_students}','{mentor_id}','{language_id}','{price}','{courses_status_id}')"""
        Database.connect(query, "insert")

    @staticmethod
    def update(table, column_name, old_data, new_data):
        query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")


    @staticmethod
    def deleted_id(tabl, id, data):
        query = f"""DELETE FROM {tabl} WHERE {id} = {data}"""
        Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        if type(data) == int:
            query = f"DELETE FROM {table} WHERE{column_name} = {data}"
        else:
            query = f"DELETE FROM {table} WHERE{column_name} = '{data}'"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")




def select_mentor(email, password):
    query = """SELECT * FROM mentor"""
    data = Database.connect(query, "select")
    for i in data:
        if i[3] == email and i[4] == password:
            print(f"""
                   ID: {i[0]}
                   First Name: {i[1]}
                   Last Name: {i[2]}
                   Email: {i[3]}
                   Password: {i[4]}
                   """)
            back = input("""
                                        1. Update
                                        0. Back
                                            >>> """)

            if back == "1":
                column_name = input("Enter your column name: ")
                old_data = input("Enter your old data: ")
                new_data = input("Enter your new data: ")
                table = 'mentor'
                if column_name.lower() == "id":
                    column_name = "mentor_id"
                    print(Student.update_id(table, column_name, old_data, new_data))
                    return select_mentor(email, password)
                elif column_name.lower() != "id":
                    print(Student.update(table, column_name, old_data, new_data))
                    print(select_mentor(email, password))
                    return select_mentor(email, password)
                else:
                    print("Invalid column")
                    return select_mentor(email, password)

            if back == "0":
                return Mentor.mentor_panel(email, password)
            else:
                print("Invalid")
                return select_mentor(email, password)


@staticmethod
def select_student(email, password):

    query = """SELECT * FROM students"""

    natija = Database.connect(query, "select")
    for i in natija:
        if i[3] == email and i[4] == password:
            print(f"""
                    ID: {i[0]}
                    First Name: {i[1]}
                    Last Name: {i[2]}
                    Email: {i[3]}
                    Password: {i[4]}
                    Balancing: {i[10]}
                    """)

            back = input("""
                        1. Update
                        0. Back
                            >>> """)

            if back == "1":
                column_name = input("Column name: ")
                old_data = input("Old data: ")
                new_data = input("New data: ")
                table = "students"
                if column_name.lower() == "id":
                    column_name = "student_id"
                    print(Student.update_id(table, column_name, old_data, new_data))
                    return select_student(email, password)
                elif column_name.lower() != "id":
                    print(Student.update(table, column_name, old_data, new_data))
                    return select_student(email, password)
                else:
                    print("Invalid column")
                    return select_student(email, password)

            if back == "0":
                return Students.student_panel(email, password)
            else:
                print("Invalid")
                return select_student(email, password)



