from operations import addStudent,viewStudent,deleteStudent,updateStudent
import sys
while True:
    print("1.add emp")
    print("2.view emp")
    print("3.update emp")
    print("4.delete emp")
    print("5.Exit")
    choice=int(input("enter option here:.."))
    if choice==1:
        addStudent()
    elif choice==2:
        viewStudent()
    elif choice==4:
        deleteStudent()
    elif choice==3:
        updateStudent()
    elif choice==5:
        print("Exist..")
        sys.exit()
    else:
        print("invalid choice")
