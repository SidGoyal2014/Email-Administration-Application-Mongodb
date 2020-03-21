import os
from email import *
from mongodb_database_opr import *

print("Enter 1 to add new entry")
print("Enter 2 to delete an entry")
print("Enter 3 to exit")
print("Enter 4 to view whole database")
print("Enter 5 to update passsword")

n = int(input())

while(n!=3):

    if(n==1):
        firstname = input("Enter firstname :")
        lastname = input("Enter Lastname :")
        department =  input("Enter department :")

        E = Email(firstname,lastname,department)

        email = E.generate_email()
        password = E.random_password_generator(16)
        print()
        E.print_data()

        D = Database()
        D.insert_data(firstname,lastname,department,email,password)

    elif(n==2):
        email = input("Enter email of that person to delete...")
        D = Database()
        D.delete_data(email)

    elif(n==3):
        print("Exit")

    elif(n==4):        
        D = Database()
        D.view_full_data()

    elif(n==5):
        email = input("Enter Email : ")
        oldpass = input("Enter old password : ")
        newpass = input("Enter new passpord : ")        
        D = Database()
        if(D.update_password(email,oldpass,newpass)):
            print()
            print("Data updated successfully")
        else:
            print()
            print("An error occurred")


    print()
    x = input("Enter any aplphabet to continue............")
    print()
    os.system('cls')

    print("Enter 1 to add new entry")
    print("Enter 2 to delete an entry")
    print("Enter 3 to exit")
    print("Enter 4 to view whole database")
    print("Enter 5 to update password")

    n = int(input())    

print("Exit")
