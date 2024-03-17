

from Class import Karzinka

def selected():
    sel = input("""
    1. Customer
    2. Praduct
    3. Worker
    0. Back
        >>> """)
    if sel == "1":
        tabl = "customer"
        data = Karzinka.select(tabl)
        for i in data:
            print(f"""
            ID: {i[0]}
            First name: {i[1]}
            Last name: {i[2]}
            Card number: {i[3]}
            """)
        return selected()
    elif sel == "2":
        tabl = "praduct"
        data = Karzinka.select(tabl)
        for i in data:
            print(f"""
            ID: {i[0]}
            Name: {i[1]}
            Price: {i[2]}
            """)
        return selected()
    elif sel == "3":
        tabl = "worker"
        data = Karzinka.select(tabl)
        for i in data:
            print(f"""
            ID: {i[0]}
            First name: {i[1]}
            Last name: {i[2]}
            Birth date: {i[3]}
            Salariy: {i[4]}
            """)
            return selected()
    elif sel == "0":
        return main()
    else:
        print("Invalid")
        return selected()

    tabl = "praduct"
    print(Karzinka.select(tabl))

def inserted():
    vibr = input("""
    1. Customer
    2. Praduct
    3. Worker
    0. Back
        >>> """)
    if vibr == "1":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        card_number = input(" Enter your card number: ")
        print(Karzinka.insert_customer(first_name, last_name, card_number))
        return inserted()
    elif vibr == "2":
        name = input("Enter praduct name: ")
        price = input("Enter praduct price: ")
        print(Karzinka.insert_praduct(name, price))
        return inserted()
    elif vibr == "3":
        first_name = input("Enter your first neme: ")
        last_name = input("Enter your last name: ")
        birth_date = input("Enter your birth date: ")
        salary = input("Enter your salary: ")
        print(Karzinka.insert_worker(first_name, last_name, birth_date, salary))
        return inserted()
    elif vibr == "0":
        return main()
    else:
        print("Invalid")
        return inserted()


def updated():
    upd = input("""
        1. Customer
        2. Praduct
        3. Worker
        0. Back
            >>> """)



def main():
    tabl = input("""
    1. SELECT 
    2. UPDATE
    3. INSERT
    4. DELETE
        >>> """)

    if tabl == "1":
        return selected()
    elif tabl == "2":
        pass
    elif tabl == "3":
        return inserted()
    elif tabl == "4":
        pass
    else:
        print("Invalid")
        return main()

if __name__ == "__main__":
    main()