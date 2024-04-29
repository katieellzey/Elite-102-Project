import mysql.connector
connection = mysql.connector.connect(
    user = "root", database = "mydb", password = "S10d3n1@pc")
cursor = connection.cursor()
import random

#declare variables
menu = ["1. Sign in", "2. Create Account", "3. Modify Account", "4. Transaction", "5. Delete Account", "6. Sign Out", "7. Exit"]
active = True
signed_in = False
current_id = 1
current_role = "empty"

#functions
def print_options():
    for i in menu:
        print(i)

def create_account():
    global current_role
    current_role = input("Are you a customer or employee: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    dob = input("Enter your date of birth(xx/xx/xxxx): ")
    email = input("Enter your email: ")
    phone_num = input("Enter your phone number: ")
    id = random.randint(100, 100000)
    #addPerson = ("INSERT INTO person (idperson, firstname, lastname, dateofbirth, email, phonenumber) VALUES(%s, %s, %s, %s, %s, %s)")
    #personVal = (id, first, last, dob, email, phone_num)
    #cursor.execute(addPerson, personVal)
    if current_role == "employee":
        position = input("What is your position: ")
        password = input("Create your password:")
        addEmployee = ("INSERT INTO employee (idperson, position, password, firstname, lastname, dateofbirth, email, phonenumber) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
        employeeVal = (id, position, password, first, last, dob, email, phone_num)
        cursor.execute(addEmployee, employeeVal)
        connection.commit()
    else:
        balance = input("Enter how much money you will deposit as your starting balance:")
        dateOpened = input("Enter today's date(xx/xx/xxxx): ")
        pin = input("Create a pin for your account: ")
        addCustomer = ("INSERT INTO customer_account (idperson, balance, date_opened, pin, firstname, lastname, dateofbirth, email, phonenumber) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        customerVal = (id, balance, dateOpened, pin, first, last, dob, email, phone_num)
        cursor.execute(addCustomer, customerVal)
        connection.commit()

def sign_in():
    global signed_in
    global current_id
    global current_role
    current_role = input("Are you a customer or employee: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    if current_role == "employee":
        password = input("Enter your password: ")
        find_account = ("SELECT idperson FROM employee WHERE firstname = %s AND lastname = %s AND password = %s")
        sign_in_values = (first, last, password)
        cursor.execute(find_account, sign_in_values)
        id = cursor.fetchall()
        signed_in = True
        current_id = id
    else:
        pin = input("Enter your pin: ")
        find_account = ("SELECT idperson FROM customer_account WHERE firstname = %s AND lastname = %s AND pin = %s")
        sign_in_values = (first, last, pin)
        cursor.execute(find_account, sign_in_values)
        id = cursor.fetchall()
        signed_in = True
        current_id = id

def modify_account():
    global signed_in
    global current_id
    global current_role
    if signed_in == True:
        if current_role == "employee":
            modify = input("What would you like to modify? position, password, email, phone number, first name, or last name? ")
            if modify == "position":
                new_pos = input("Enter your new position: ")
                sql = "UPDATE employee SET position = %s WHERE idperson = %s"
                val = (new_pos, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "password":
                new_pass = input("Enter your new password: ")
                sql = "UPDATE employee SET password = %s WHERE idperson = %s"
                val = (new_pass, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "email":
                new_email = input("Enter your new email: ")
                sql = "UPDATE employee SET email = %s WHERE idperson = %s"
                val = (new_email, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "phone number":
                new_phone = input("Enter your new phone number: ")
                sql = "UPDATE employee SET phonenumber = %s WHERE idperson = %s"
                val = (new_phone, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "first name":
                new_first = input("Enter your new first name: ")
                sql = "UPDATE employee SET firstname = %s WHERE idperson = %s"
                val = (new_first, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "last name":
                new_last = input("Enter your new last name: ")
                sql = "UPDATE employee SET lastname = %s WHERE idperson = %s"
                val = (new_last, current_id)
                cursor.execute(sql, val)
                connection.commit()
            else:
                print("Invalid response.")
        else:
            modify = input("What would you like to modify? pin, email, phone number, first name, or last name?")
            if modify == "pin":
                new_pin = input("Enter your new pin: ")
                sql = "UPDATE employee SET password = %s WHERE idperson = %s"
                val = (new_pin, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "email":
                new_email = input("Enter your new email: ")
                sql = "UPDATE employee SET email = %s WHERE idperson = %s"
                val = (new_email, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "phone number":
                new_phone = input("Enter your new phone number: ")
                sql = "UPDATE employee SET phonenumber = %s WHERE idperson = %s"
                val = (new_phone, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "first name":
                new_first = input("Enter your new first name: ")
                sql = "UPDATE employee SET firstname = %s WHERE idperson = %s"
                val = (new_first, current_id)
                cursor.execute(sql, val)
                connection.commit()
            elif modify == "last name":
                new_last = input("Enter your new last name: ")
                sql = "UPDATE employee SET lastname = %s WHERE idperson = %s"
                val = (new_last, current_id)
                cursor.execute(sql, val)
                connection.commit()
            else:
                print("Invalid response.")
    else:
        print("You must be signed in first.")

def transaction():
    global signed_in
    global current_id
    global current_role
    if signed_in == True:
        if current_role == "customer":
            view_balance = input("Here is your current balance: ")
            get_balance = "SELECT balance FROM customer_account WHERE idperson = %s"
            cursor.execute(get_balance, current_id)
            balance = cursor.fetchall()
            print(balance)
            transaction_type = input("Would you like to withdraw or deposit?")
            if transaction_type == "withdraw":
                withdraw = input("How much would you like to withdraw?")
                new_balance = balance - withdraw
                update_balance = "UPDATE customer_account SET balance = %s WHERE idperson = %s"
                vals = (new_balance, current_id)
                cursor.execute(update_balance, vals)
                connection.commit()
            else:
                deposit = input("How much would you like to deposit?")
                new_balance = balance + deposit
                update_balance = "UPDATE customer_account SET balance = %s WHERE idperson = %s"
                vals = (new_balance, current_id)
                cursor.execute(update_balance, vals)
                connection.commit()
        else:
            print("This option is only for customers.")
    else:
        print("You must be signed in first.")

def delete_account():
    global signed_in
    global current_id
    global current_role
    delete = input("Would you like to delete your account, yes or no?")
    if signed_in == True:
        if delete == "yes":
            if current_role == "employee":
                test_pass = input("Enter your password to confirm deletion: ")
                find_pass = ("SELECT password FROM employee WHERE idperson = %s")
                idval = (current_id)
                cursor.execute(find_pass, idval)
                password = cursor.fetchall()
                if password == test_pass:
                    remove = "DELETE FROM employee WHERE idperson = %s"
                    idval = (current_id)
                    cursor.execute(remove, idval)
                else:
                    print("Password doesn't match. Account can't be deleted.")
            else:
                test_pin = input("Enter your pin to confirm deletion: ")
                find_pin = ("SELECT pin FROM customer_account WHERE idperson = %s")
                idval = (current_id)
                cursor.execute(find_pin, idval)
                pin = cursor.fetchall()
                if pin == test_pin:
                    remove = "DELETE FROM customer_account WHERE idperson = %s"
                    idval = (current_id)
                    cursor.execute(remove, idval)
                else:
                    print("Pin doesn't match. Account can't be deleted.")
    else:
        print("You must be signed in first.")

def sign_out():
    global signed_in
    global current_id
    global current_role
    if signed_in == True:
        current_id = 0
        current_role = "empty"
        signed_in = False
    else:
        print("You are not signed in.")


print("Hello and welcome to the online banking program.")
while active:
    print_options()
    user_choice = input("Enter the number correlating to your choice: ")
    if user_choice == "1":
        sign_in()
    elif user_choice == "2":
        create_account()
    elif user_choice == "3":
        modify_account()
    elif user_choice == "4":
        transaction()
    elif user_choice == "5":
        delete_account()
    elif user_choice == "6":
        sign_out()
    elif user_choice == "7":
        leave = input("Would you like to exit? yes or no? ")
        if leave == "yes":
            active = False
    else:
        print("Invalid. Please answer with a number. ")

