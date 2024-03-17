from database_db import Database

def creates_table():
    mentor_table = """
       CREATE TABLE mentor (
           mentor_id SERIAL PRIMARY KEY,
           first_name VARCHAR(20),
           last_name VARCHAR(20),
           email VARCHAR(50),
           password VARCHAR(8),
           headline CHAR,
           bio VARCHAR(200),
           contact_url VARCHAR(200),
           last_update DATE DEFAULT now(),
           create_date TIMESTAMP DEFAULT now()
       );"""

    language_table = """
        CREATE TABLE language (
            language_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now()
        );"""

    courses_status_table = """
        CREATE TABLE courses_status (
            courses_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date TIMESTAMP DEFAULT now()
        );"""

    courses_table = """
        CREATE TABLE courses (
            courses_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            description VARCHAR(50),
            rating FLOAT,
            active_students INT,
            mentor_id INT REFERENCES mentor(mentor_id),
            language_id INT REFERENCES language(language_id),
            price SMALLINT,
            courses_status_id INT REFERENCES courses_status(courses_status_id),
            support_date TEXT,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now()
        );"""

    modul_table = """
        CREATE TABLE modul (
            modul_id SERIAL PRIMARY KEY,
            courses_id INT REFERENCES courses(courses_id),
            lesson_count SMALLINT,
            last_updated DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now()
        );"""

    lesson_status_table = """
        CREATE TABLE lesson_status (
            lesson_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date TIMESTAMP DEFAULT now()
        );"""

    lesson_table = """
        CREATE TABLE lesson (
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            description VARCHAR(50),
            lesson_status_id INT REFERENCES lesson_status(lesson_status_id),
            modul_id INT REFERENCES modul(modul_id),
            create_date TIMESTAMP DEFAULT now()
        );"""



    students_table = """
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            email VARCHAR(50),
            password CHAR,
            headline VARCHAR(100),
            bio VARCHAR(100),
            contact_url VARCHAR(100),
            last_updated DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now()
        );"""

    payment = """
        CREATE TABLE payment (
            payment_id SERIAL PRIMARY KEY,
            courses_id INT REFERENCES courses(courses_id),
            student_id INT REFERENCES students(student_id),
            amount INT,
            card_number VARCHAR(20),
            create_date TIMESTAMP DEFAULT now()
        );"""


    payment_status = """
    CREATE TABLE payment_status (
    payment_status_id SERIAL PRIMARY KEY,
    status TEXT,
    create_date TIMESTAMP DEFAULT now());"""



    comment_table = """
        CREATE TABLE comment (
            comment_id SERIAL PRIMARY KEY,
            text TEXT,
            student_id INT REFERENCES students(student_id),
            courses_id INT REFERENCES courses(courses_id),
            create_date TIMESTAMP DEFAULT now()
        );"""

    data = {
        "mentor_table": mentor_table,
        "language_table": language_table,
        "courses_status_table": courses_status_table,
        "courses_table": courses_table,
        "lesson_status_table": lesson_status_table,
        "modul_table": modul_table,
        "lesson_table": lesson_table,
        "payment_status": payment_status,
        "students_table": students_table,
        "payment": payment,
        "comment_table": comment_table
    }

    for i in data:
        print(f"{i} => {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    creates_table()
