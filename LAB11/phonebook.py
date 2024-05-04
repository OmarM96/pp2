from tkinter import EXCEPTION
import psycopg2, platform, os, csv
from config import host, user, password, db_name
def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
  
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░██████╦╝██║░░██║██║░░██║█████═╝░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██╔══██╗██║░░██║██║░░██║██╔═██╗░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝
                                                                                                                                                                                                    
                        By : Muratkan Aldiyar 
""")   

def delete(PNumber):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
            f"delete from PhoneBook where PhoneNumber = '{PNumber}'"
            )
            print("[INFO] Deleting was complete siccesfully!")
        except Exception as ex:
            print(f"[INFO] Error, deleting is failed - {ex}")

def insert(username, PNumber):
    username = username.strip()
    PNumber = PNumber.strip()
    #print(PNumber)
    with conn.cursor() as cursor:
        try:
            cursor.execute(
            f"insert into PhoneBook (username, PhoneNumber) values ('{username}','{PNumber}')"
            )
            print ("[INFO] Insert was complete succesfully!")
        except Exception as ex:
            print(f"[INFO] Error, iserting is failed - {ex}")

try:
    banner()
    conn = psycopg2.connect(
        database=db_name, 
        user=user, 
        password=password, 
        host=host)    
    #cursor = conn.cursor()
    conn.autocommit = True #autocommit

    with conn.cursor() as cursor:
        #inp = input("pattern")
        #cursor.callproc('find_word',[inp])
        #print(cursor.fetchall())
        pass
        #cursor.callproc("add_update_user",['Damir','1234'])
    
    with conn.cursor() as cursor:
        with open('data.csv', "r", encoding="utf-8") as data:
            printed_data = list(csv.reader(data))
            cursor.callproc('insertlist', printed_data)

    #pagination
    with conn.cursor() as cursor:
        limit = input('limit')
        offset = input('Offset')

        cursor.callproc('getAll',(limit,offset))
        print(cursor.fetchall())
    
    #insert and update
    with conn.cursor() as cursor:
        name = input('name')
        number = input('Number')

        cursor.execute(f"CALL add_update_user('{name}','{number}')")
        print(cursor.fetchall())

except Exception as _ex:
    print ("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if conn:
        #cursor.close()
        conn.close()
        print ("[INFO] Postgre connection closed")
