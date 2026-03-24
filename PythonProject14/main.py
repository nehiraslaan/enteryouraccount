
defusername = "Dzintars"
defpassword = "Nehir"

while (True):
     username = input("Username: ")
     password = input("Password: ")
     if username == defusername and password == defpassword:
         print("Welcome " , username + "!")
         break

     elif username != defusername and password == defpassword:
         print("Wrong username!")

     elif username == defusername and password != defpassword:
         print("Wrong password!")
         print("Do you want to change your password? (Y/N)")
         answer = input()
         if answer == "Y" or reset == "y":
             newpassword = input("New Password: ")
             defpassword= newpassword
             print("Please,wait...")
             print("Password has been changed successfully!")

         else:
             print("Login Failed, try again!")
