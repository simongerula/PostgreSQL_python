import psycopg2
from os import system
import time

# HOME
def home():
    system("cls")
    print("| CRUD POSTGRESQL WITH PYTHON |")
    print("|      CREATE TABLE [1]       |")
    print("|        READ TABLE [2]       |")
    print("|     UPGRADE TABLE [3]       |")
    print("|      DELETE TABLE [4]       |")


    
    menu_sel = int(input("..."))

    if menu_sel == 1 :
        create_table()
    elif menu_sel == 2 :
        read_table()
    elif menu_sel == 3 :
        update_table()
    elif menu_sel == 4 :
        delete_table()
    else :
        print("WRONG OPTION")
        input("PRESS ENTER TO RETURN HOME")
        home()

# CREATE
def create_table():
    table_name = input("TABLE NAME: ")
    ctn_col = int(input("N° OF COLUMNS: "))
    if ctn_col > 0 :
        cont = 1
        if cont == 1 :
                col_name = input("COLUMN #%s HEADER: " %(cont))
                col_type = input("COLUMN #%s TYPE: " %(cont))
                cont += 1
                conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
                cursor = conn.cursor()
                query = '''CREATE TABLE %s (%s %s);''' %(table_name, col_name, col_type)
                cursor.execute(query)
                conn.commit()
                if ctn_col == 1:
                    conn.close()
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("... TABLE CREATED")
                    input("PRESS ENTER TO RETURN HOME")
                    home()

        if cont > 1 :
            for i in range((ctn_col)-(1)):
                print("")
                col_name = input("COLUMN HEADER: ")
                col_type = input("VALUE TYPE: ")
                query = '''ALTER TABLE %s ADD %s %s;''' %(table_name, col_name, col_type)
                cursor.execute(query)
                conn.commit()
            conn.close()
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("... TABLE CREATED")
            input("PRESS ENTER TO RETURN HOME")
            home()

    elif ctn_col == 0 :
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''CREATE TABLE %s ();''' %(table_name)
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("... TABLE CREATED")
        input("PRESS ENTER TO RETURN HOME")
        home()


# UPDATE
def update_table():
    print("|        ADD COLUMN [1]       |")
    print("|     RENAME COLUMN [2]       |")
    print("|     INSERT VALUES [3]       |")
    print("|     DELETE VALUES [4]       |")
    updt_sel = int(input("..."))
    if updt_sel == 1 :
        add_column()
    elif updt_sel == 2 :
        rename_column()
    elif updt_sel == 3 :
        insert_value()
    elif updt_sel == 4:
        delete_values()


# ADD COLUMN
def add_column():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    table_name = input("TABLE NAME: ")
    ctn_col = int(input("N° OF COLUMNS: "))
    for i in range(ctn_col):
        print("")
        col_name = input("COLUMN HEADER: ")
        col_type = input("VALUE TYPE: ")
        query = '''ALTER TABLE %s ADD %s %s;''' %(table_name, col_name, col_type)
        cursor.execute(query)
        conn.commit()
    conn.close()
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("... COLUMN(S) CREATED")
    input("PRESS ENTER TO RETURN HOME")
    home()


# RENAME COLUMN
def rename_column():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    table_name = input("TABLE NAME: ")
    col_name = input("COLUMN NAME: ")
    ncol_name = input("NEW COLUMN NAME: ")
    print("")
    query = '''ALTER TABLE %s RENAME COLUMN %s TO %s;''' %(table_name, col_name, ncol_name)
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("... COLUMN RENAMED")
    input("PRESS ENTER TO RETURN HOME")
    home()

# INSERT VALUE
def insert_value():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    print("SHOW TABLE INFO")
    table_name = input("TABLE NAME: ")
    query = '''select column_name, data_type from information_schema.columns where table_name = '%s';''' %(table_name)
    cursor.execute(query)
    print(cursor.fetchall())
    ctn_col = int(input("N° OF COLUMNS TO FILL: "))
    if ctn_col == 1 :
        print("")
        col_name = input("COLUMN NAME: ")
        col_value = input("VALUE: ")
        query = '''INSERT INTO %s (%s) VALUES (%s);''' %(table_name, col_name, col_value)
        cursor.execute(query)
    elif ctn_col == 2:
        col_name = input("COLUMN NAME: ")
        col_value = input("VALUE: ")
        print("")
        col_name2 = input("COLUMN NAME: ")
        col_value2 = input("VALUE: ")
        query = '''INSERT INTO %s (%s, %s) VALUES (%s, %s);''' %(table_name, col_name, col_name2, col_value, col_value2)
        cursor.execute(query)
    elif ctn_col == 3:
        col_name = input("COLUMN NAME: ")
        col_value = input("VALUE: ")
        print("")
        col_name2 = input("COLUMN NAME: ")
        col_value2 = input("VALUE: ")
        print("")
        col_name3 = input("COLUMN NAME: ")
        col_value3 = input("VALUE: ")
        query = '''INSERT INTO %s (%s, %s, %s) VALUES (%s, %s, %s);''' %(table_name, col_name, col_name2, col_name3, col_value, col_value2, col_value3)
        cursor.execute(query)
    elif ctn_col == 4:
        col_name = input("COLUMN NAME: ")
        col_value = input("VALUE: ")
        print("")
        col_name2 = input("COLUMN NAME: ")
        col_value2 = input("VALUE: ")
        print("")
        col_name3 = input("COLUMN NAME: ")
        col_value3 = input("VALUE: ")
        print("")
        col_name4 = input("COLUMN NAME: ")
        col_value4 = input("VALUE: ")
        query = '''INSERT INTO %s (%s, %s, %s) VALUES (%s, %s, %s);''' %(table_name, col_name, col_name2, col_name3, col_name4, col_value, col_value2, col_value3, col_value4)
        cursor.execute(query)
    else:
        print("MAX 4 COLUMNS FOR NOW")
    conn.commit()
    conn.close()
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("... VALUES ADDED")
    input("PRESS ENTER TO RETURN HOME")
    home()

# DELETE VALUES
def delete_values():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    print("SHOW TABLE INFO")
    table_name = input("TABLE NAME: ")
    print("")
    query = '''SELECT * FROM %s''' %(table_name)
    cursor.execute(query)
    for i in query:
        if (cursor.fetchone() != "None") :
            print(cursor.fetchone())
    print("")
    id = int(input("ID TO DELETE: "))
    query = '''DELETE FROM %s WHERE id=%s;''' %(table_name, id)
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("... VALUES DELETED")
    input("PRESS ENTER TO RETURN HOME")
    home()

# READ TABLE
def read_table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    table_name = input("TABLE NAME: ")
    query = '''select column_name, data_type from information_schema.columns where table_name = '%s';''' %(table_name)
    cursor.execute(query)
    print(cursor.fetchall())
    parameter = input("PARAMETER TO SEARCH: ")
    key = input("KEY WORD: ")
    print("")
    query = '''SELECT * FROM %s WHERE %s=%s;''' %(table_name, parameter, key)
    cursor.execute(query)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("... VALUES FOUNDED")
    #for i in query:
    #    print(cursor.fetchone())
    print(cursor.fetchall())
    conn.commit()
    conn.close()
    input("PRESS ENTER TO RETURN HOME")
    home()

# DELETE TABLE
def delete_table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conn.cursor()
    table_name = input("TABLE NAME: ")
    check = input("SURE TO DELETE TABLE? (Y/n): ")
    if check.upper() == "Y":
        query = '''DROP TABLE %s''' %(table_name)
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("... TABLE DELETED")
        input("PRESS ENTER TO RETURN HOME")
        home()
    else:
        home()




home()



