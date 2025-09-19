from authentication import signup,login
print("1. signup")
print("2. login")
print("3. exit")

choose=input("choose above options any one :-- ")
if choose == "1":
    signup()
elif choose == "2":
    login()  