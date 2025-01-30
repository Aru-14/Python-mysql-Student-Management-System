# Arunima Paunikar 
#project

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@14aug",
    auth_plugin="mysql_native_password",
    database = "DB_4_1"

)
print(mydb)
print(mydb.connection_id)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENTS1(NAME VARCHAR(20), ROLL_NO INT)")

def show():
     mycursor.execute("SELECT * FROM STUDENTS1")
     result = mycursor.fetchall()
     if result == []:
        print("No student found. Please enter a student")
        
     else:
        for x in result:
            print(x)

def add():
    name = input("Enter the name:")
    roll_no = int(input("Enter the roll_no"))
    sql = ("INSERT INTO STUDENTS1 VALUES(%s,%s)")
    values = (name, roll_no)
    mycursor.execute(sql,values)
    mydb.commit()
    print(mycursor.rowcount,"Student inserted successfully")


def remove():
    name = input("Enter student name to delete")
    sql = "DELETE FROM STUDENTS1 WHERE NAME = %s"
    mycursor.execute(sql,(name,))
    mydb.commit()
    print(f"Deleted {name} successfully")
    
def update():
        print("Enter the choice: \n 1.Update name \n 2.Update roll_no ")
        choice = int(input("\n"))
        
        if choice == 2:
            roll_no1 = int(input("Enter the roll_no to update"))
            roll_no = int(input("Enter the roll_no to set"))
            sql = "UPDATE STUDENTS1 SET ROLL_NO = %s WHERE ROLL_NO = %s"
            mycursor.execute(sql,(roll_no,roll_no1))
            mydb.commit()
            print(f"Updated the {roll_no1} successfully")
        elif choice == 1:
            name1 = (input("Enter the name to update"))
            name = (input("Enter the name to set"))
            sql = "UPDATE STUDENTS1 SET NAME = %s WHERE NAME = %s"
            mycursor.execute(sql,(name,name1))
            mydb.commit()
            print(f"Updated the {name1} successfully")
            
while(1):
    print("**----Welcome to Classroom----**")
    print("Enter the choice: \n 1.View all students \n 2.Add new Student \n 3.Remove Student \n 4.Update information of student \n 5.Exit")
    choice = int(input("\n"))
    if choice == 1:
        show()
    elif choice == 2:
        add()   
    elif choice == 3:
        remove()     
    elif choice == 4:
        update()
    elif choice == 5:
        print("Exited")
        exit()    
    else:
        print("Invalid entry")    