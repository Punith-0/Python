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
        return cur.fetchall() if cur.description else None
    except psycopg2.Error as e :
        print("Error while executing query", e)

def display(rows) :
    try :
        print("The Table contents are :")
        print("*" * 15)
        for i , row in enumerate(rows , 1) :
            print(f"{i:>4} | {row}")
        print("*" * 15)
    except Exception as e :
        print("Error while fetching data", e)

def main() :
    conn =connection()
    if not conn :
        print("connot create a connection ")
        return
    cur = cursor(conn)
    if not cur :
        print("connot create a connection ")
        return
    while True :
        query = input("Enter query :").strip()
        query = " ".join(query.split())
        if query.lower() in ['exit' , 'quit' , 'q'] :
            break
        if query.lower() in ['cls' , 'clear'] :
            os.system('cls' if os.name == 'nt' else 'clear' )
            continue
        if query.startswith(r'\c'):
            p = query.split()
            if len(p) < 2 :
                print("Usage : \\c <database>")
                continue
            db =  query.split()[-1].strip(';')
            close(conn , cur)
            conn = connection_db(db)
            if not conn :
                print("connot create a connection ")
                continue
            cur = cursor(conn)
            if cur :
                print(f"Connected to database {db}")
            continue
        rows = execute_query(cur , query)
        if rows is None:
            print("Done")
        elif not rows :
            print("No rows found")
        else :
            display(rows)
        
    close(conn , cur)


if __name__ == "__main__" :
    main()
