print("""
****************

Welcome to MY website...

Sign-in Side

""")

c= input("Do you want to create an account?")

if c== "yes":
    Username=input("Enter Your username Please:")
    User_password=input("Enter Your Password Please:")
    Accounts=open("useraccount.txt", "r+")
    Accounts.write(Username + "\n" + User_password)
    print("You created an account")

print("*************** Please Login ************")

sys_user_name = input("Enter your Username:") # Kullanıcı Adını input ile alıyoruz.

sys_password =input("Enter Your Password:")

Accounts = open('useraccount.txt', "r").readlines()

Username = Accounts[0].strip()
Password = Accounts[1].strip()

if (Username != sys_user_name and Password == sys_password):
    print("Wrong User name...")
elif (Username == sys_user_name and Password != sys_password):
    print("Wrong Password...")

elif (Username != sys_user_name and Password != sys_password):
    print("Wrong Username and Password...")

else:
    print("You logined")
