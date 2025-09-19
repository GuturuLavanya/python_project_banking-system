from db import get_connection
import sys
connectionTODB=get_connection()
cur=connectionTODB.cursor()
def addStudent():
    # connectionTODB=get_connection()
    std_ids=int(input("enter a student id:.."))
    std_names=input("enter a student name:..")
    std_branchs=input("enter a student branch:..")
    std_emails=input("enter a student email:..")
    std_phone=int(input("enter student phonenumber"))
    print("added Student")
    # connectionTODB=get_connection()
    # cur=connectionTODB.cursor()
    cur.execute("insert into Students(std_id,std_name,std_branch,std_email,std_phonenum)values(%s,%s,%s,%s,%s)",(std_ids,std_names,std_branchs,std_emails,std_phone))
    connectionTODB.commit()
    connectionTODB.close()
    print(f"{std_names} added successfully")

def viewStudent():
    cur.execute("select * from Students")
    # print(cur.fetchall())
    data=cur.fetchall()
    # for i in data:
    #     print(i)
    # for i in data:
    #     for j in i:
    #         print(j)
    for i in data:
        print(i[1])
    connectionTODB.close()
    print(f" student data fetched  successfully")
    
def deleteStudent():
    std_id=int(input("enter a id:.."))
    cur.execute("delete from Students where std_id=%s",(std_id,))
    connectionTODB.commit()
    connectionTODB.close()
# def updateStudent():
#     std_id=int(input("enter a std id:.."))
#     std_name=input("enter a std name:..")
#     std_branch=input("enter update branch:..")
#     cur.execute("update Students set std_name=%s,std_branch=%s where std_id=%s",(std_name,std_branch,std_id,))
#     connectionTODB.commit()
#     connectionTODB.close()
def updateStudent():

        # std_id = int(input("Enter student ID to update: "))

    while True:
        std_id = int(input("Enter student ID to update: "))
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Branch")
        print("3. Email")
        print("4.phonenum")
        print("5.exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            std_name = input("Enter new name: ")
            cur.execute("UPDATE students SET std_name=%s WHERE std_id=%s", (std_name, std_id))

        elif choice == 2:
            std_branch = input("Enter new branch: ")
            cur.execute("UPDATE students SET std_branch=%s WHERE std_id=%s", (std_branch, std_id))

        elif choice == 3:
            std_email = input("Enter new email: ")
        
            cur.execute("UPDATE students SET std_name=%s, std_branch=%s WHERE std_id=%s",
                    (std_email, std_id))
        elif choice==4:
            std_phonenum=input("Enter new phonenumber:")
            cur.execute("UPDATE students SET std_name=%s, std_branch=%s WHERE std_id=%s",
                    (std_phonenum, std_id))
        elif choice==5:
            print("exit..")
            sys.exit()


        else:
            print("Invalid choice!")

        connectionTODB.commit()
        print("✅ Record updated successfully!")


    
