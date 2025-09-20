from authentication import signup,login
from customer_menu import withdraw,deposit,check_bal,request
from admin_menu import search_customer,delete_customer,search_admin,fetchUsers,viewReqs
print("1. signup")
print("2. login")
print("3. exit")

choose=input("choose above options any one :-- ")
if choose == "1":
    signup()
elif choose == "2":
    abc=login() 
    user_id,user_name,user_pswd,user_role=abc
    # print(user_role)
    if user_role=="customer":
        print(".....customer menu.....")
        print("1,withdraw")
        print("2.deposite")
        print("3.check_bal")
        print("4.request (atm/loan/checkbook)")
        choose=int(input("enter option here:.."))
        if choose==1:
            withdraw(user_id)
        elif choose==2:
            deposit(user_id)
        elif choose==3:
            check_bal(user_id)
        elif choose==4:
            request(user_id)

    if user_role =="admin":
       


        while True:
            print("--------admin features----------") 
            print("1.search for customer")
            print("2.search for admin")
            print("3.fetch all users")
            print("4.delete  customer")
            print("5.view requests for customer")

            choose =int(input("enter yr option here :----    "))
            if choose == 1:
                search_customer()
            elif choose ==2:
                search_admin()  
            elif choose == 3:

                fetchUsers()   
            elif choose == 4:
                delete_customer() 
                 
            else:
                viewReqs() 

