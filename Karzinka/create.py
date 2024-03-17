from database_db import Database

def create_table():

    category_table = """
    CREATE TABLE  category (
    categoriy_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());"""

    praduct_table = """
    CREATE TABLE praduct (
    praduct_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    price INT,
    last_update DATE DEFAULT now(),
    create_date TIMESTAMP DEFAULT now());"""

    product_categoriy_table = """
    CREATE TABLE product_categoriy (
    product_categoriy_id SERIAL PRIMARY KEY,
    praduct_id INT REFERENCES praduct(praduct_id),
    categoriy_id INT REFERENCES category(categoriy_id),
    create_date TIMESTAMP DEFAULT now());"""


    payment_table = """
    CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    status VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());"""


    customer_table = """
    CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    card_number BIGINT,
    create_date TIMESTAMP DEFAULT now());"""

    payment_categoriy_table = """
    CREATE TABLE payment_category (
    payment_category_id SERIAL PRIMARY KEY,
    payment_id INT REFERENCES payment(payment_id),
    customer_id INT REFERENCES customer(customer_id),
    categoriy VARCHAR(20));"""

    speciality_table = """
    CREATE TABLE speciality (
    speciality_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now())"""

    worker_table = """
    CREATE TABLE worker (
    worker_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    birth_date DATE DEFAULT now(),
    salariy INT,
    speciality_id INT REFERENCES speciality(speciality_id),
    create_date TIMESTAMP DEFAULT now());"""


    data = {
        "category_table": category_table,
        "praduct_table": praduct_table,
        "product_categoriy_table": product_categoriy_table,
        "payment_table": payment_table,
        "customer_table": customer_table,
        "payment_categoriy_table": payment_categoriy_table,
        "speciality_table": speciality_table,
        "worker_table": worker_table
    }
    for i in data:
        print(f"{i} => {Database.connect(data[i], 'create')}")


if __name__ == "__main__":
    create_table()

