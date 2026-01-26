import psycopg2
import re
import os 

def connection() :
    try :
        conn = psycopg2.connect(
            host = "localhost" ,
            user = "postgres" ,
            password = "punit000" ,
            dbname = "postgres" ,
            port = "5432" 
        )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e :
        print("Error while connecting to PostgreSQL", e)
        return None
    
def connection_db(dbname :str) :
    try :
        conn = psycopg2.connect(
            host = "localhost" ,
            user = "postgres" ,
            password = "punit000" ,
            dbname = "".join(dbname.split()) ,
            port = "5432" 
        )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e :
        print("Error while connecting to PostgreSQL", e)
        return None
    
def cursor(conn) :
    try :
        cur = conn.cursor() if conn else None
        return cur
    except psycopg2.Error as e :
        print("Error while creating cursor", e)
        return None
    
def close(conn , cur) :
    try :
        (cur.close() if cur else None)
        (conn.close() if conn else None)
    except psycopg2.Error as e :
        print("Error while closing connection or cursor", e)

def execute_query(cur , query : str) :
    try :
        cur.execute(query)
    except psycopg2.Error as e :
        print("Error while executing query", e)



def main() :
    conn =connection()
    cur = cursor(conn)
    while True :
        query = input("Enter query :").strip()
        query = " ".join(query.split())
        if query.lower() in ['exit' , 'quit' , 'q'] :
            break
        if query.lower() == r'cls' or query.lower() == 'clear' :
            os.system('cls' if os.name == 'nt' else 'clear' )
            continue
        if query.startswith(r'\c'):
            close(conn , cur)
            conn = connection_db(query.split()[-1].strip(';'))
            cur = cursor(conn)
            if conn :
                print(f"Connected to database {query.split()[-1]}")
            continue
        execute_query(cur , query)
    close(conn , cur)


if __name__ == "__main__" :
    main()
