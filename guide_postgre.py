Instalar pip install psycopg2, para poder conectar la BBDD PostgreSQL

import psycopg2

Conectar PostgreeSQL > 
    psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
