
import re
from os import system
import mysql.connector
# Note: This project requires MySQL to run, therefore it is recommended to install MySQL and then attempt to run or Debug the file.

con = mysql.connector.connect(
    host="LocalHost", user="TBTS-emp-001", password="TBTS-emp-pwd-4761"
    )
# The username and passwords in this code are fake, and actual employee usernames and passwords will be given differently, and are not the same.

cursor_object = con.cursor()
cursor_object.execute("Create new database for Employee")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Pattern = re.compile("(0|91)?[7-9][0-9]{9}") # This code is for validating a Phone Number.


def Add_Employee(): # Functions to Add_Employee.

    print("{:>60}".format("Add new Employee Record"))

    Id = input("Enter Employee Id: ")
    if (check_employee(Id) is True):
        print("This Employee ID Already Exists!\nPlease try again.")
        press = input("Press any key to Continue.")
        Add_Employee()

    Name = input("Enter Employee Name: ")
    if (check_employee_name(Name) is True):
        print("Employee Name Already Exists!\nPlease try again.")
        press = input("Press any key to Continue.")
        Add_Employee()

    email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, email_Id)):
        print("Valid Email.")
    else:
        print("Invalid Email!\nPlease try again.")
        press = input("Press any key to Continue.")
        Add_Employee()

    phone_No = input("Enter Employee Phone Number: ")
    if(Pattern.match(phone_No)):
        print("Valid Phone Number.")
    else:
        print("Invalid Phone Number!\nPlease try again.")
        press = input("Press Any Key To Continue.")
        Add_Employee()

    Address = input("Enter Employee Address: ")
    if(re.fullmatch(regex, Address)):
        print("Valid Address.")
    else:
        print("Invalid Address!\nPlease try again.")
        press = input("Press any key to Continue.")
        Add_Employee()

    Salary = input("Enter Employee Salary: ") # The salary for an employee may differ from one employee to another, so the values present in this code are not to be taken as actual values.
    if(re.fullmatch(regex, Salary)):
        print("Valid Salary.")
    else:
        print("Invalid Salary details!\nPlease try again.")
        press = input("Press any key to Continue.")
        Add_Employee()

    data = (Id, Name, email_Id, phone_No, Address, Salary)

    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)

    con.commit()
    print("Successfully Added Employee Record!")
    press = input("Press Any Key To Continue.")
    menu()

def check_employee_name(employee_name):

    sql = 'select * from empdata where Name=%s'

    c = con.cursor(buffered=True)
    data = (employee_name,)
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_(employee_id):

    sql = 'select * from empdata where Id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def Display_Employee(): # Function to Display_Employee.

    print("{:>60}".format("Display Employee Records"))

    sql = 'select * from empdata'
    c = con.cursor()
    c.execute(sql)

    # Fetching all details of the Employee.
    r = c.fetchall()
    for i in r:
        print("Employee Id: \n", i[0])
        print("Employee Name: \n", i[1])
        print("Employee Email Id: \n", i[2])
        print("Employee Phone Number: \n", i[3])
        print("Employee Address: \n", i[4])
        print("Employee Post: \n", i[5])
        print("Employee Salary: \n", i[6])
        print("\n")
    press = input("Press Any key To Continue.")
    menu()

def Update_Employee(): # Function to Update_Employee.

    print("{:>60}".format("Update Employee Record\n"))

    Id = input("Enter Employee Id: ")
    if(check_employee(Id) is False):
        print("Employee Record doesn't exist!\nPlease try again.")
        press = input("Press Any Key To Continue.")
        menu()
    else:
        email_Id = input("Enter Employee Email ID: ")

    if(re.fullmatch(regex, email_Id)):
            print("Valid Email.")
    else:
            print("Invalid Email!\nPlease try again.")
            press = input("Press Any Key To Continue.")
            Update_Employee()

    if(Pattern.match(Phone_no)):
            Phone_no = input("Enter Employee Phone Number: ")
            print("Valid Phone Number.")
    else:
            print("Invalid Phone Number!\nPlease try again.")
            press = input("Press Any Key To Continue.")
            Update_Employee()

    if (Pattern.match(Phone_no)):
            Address = input("Enter Employee Address: ")
            print("Valid Address.")
    else:
            print("Invalid Address!\nPlease try again.")
            press = input("Press Any Key To Continue.")
            Update_Employee()

sql = 'UPDATE empdata set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
data = (email_Id, phone_No, Address, Id)
c = con.cursor()
c.execute(sql, data)

con.commit()
print("Updated Employee Record")
press = input("Press Any Key To Continue..")
menu()

def Promote_Employee(): # Function to Promote_Employ.

    print("{:>60}".format("Promote Employee\n"))

    Id = input("Enter Employee Id: ")
    if(check_employee(Id) is False):
        print("Employee Record doesn't exist!\nPlease try again.")
        press = input("Press Any Key To Continue.")
        menu()
    else:
        Amount  = int(input("Enter Salary high: "))

        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)

        r = c.fetchone()
        t = r[0]+Amount

        sql = 'update empdata set Salary = %s where Id = %s'
        d = (t, Id)
        c.execute(sql, d)

        con.commit()
        print("Employee is Promoted!")
        press = input("Press Any key To Continue.")
        menu()

def Remove_Employee(): # Function to Remove_Employee.

    print("{:>60}".format("Remove Employee Record\n"))

    Id = input("Enter Employee Id: ")
    if(check_employee(Id) is False):
        print("Employee Record doesn't exist!\nPlease try again.")
        press = input("Press Any Key To Continue.")
        menu()
    else:
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)

        con.commit()
        print("Employee is Removed!")
        press = input("Press Any key To Continue.")
        menu()

def Search_Employee(): # Function to Search_Employee.

    print("{:>60}".format("Search Employee Record\n"))

    Id = input("Enter Employee Id: ")
    if(check_employee(Id) is False):
        print("Employee Record doesn't exist!!\nPlease try again.")
        press = input("Press Any Key To Continue.")
        menu()
    else:
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql, data)

        #Fetching all details of the employee.
        r = c.fetchall()
        for i in r:
            print("Employee Id: \n", i[0])
            print("Employee Name: \n", i[1])
            print("Employee Email Id: \n", i[2])
            print("Employee Phone Number: \n", i[3])
            print("Employee Address: \n", i[4])
            print("Employee Post: \n", i[5])
            print("Employee Salary: \n", i[6])

        press = input("Press Any key To Continue.")
        menu()

def menu():

    system("cls")

    print("{:>60}".format("EMPLOYEE MANAGEMENT SYSTEM\n"))
    print("{:>30}".format("version-0.2.0\n"))

    print("1. Add Employee\n")
    print("2. Display Employee Record\n")
    print("3. Update Employee Record\n")
    print("4. Promote Employee Record\n")
    print("5. Remove Employee Record\n")
    print("6. Search Employee Record\n")
    print("7. Exit\n")

    print("{:>60}".format("Array: (1/2/3/4/5/6/7)"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employee()
    elif ch == 2:
        system("cls")
        Display_Employee()
    elif ch == 3:
        system("cls")
        Update_Employee()
    elif ch == 4:
        system("cls")
        Promote_Employee()
    elif ch == 5:
        system("cls")
        Remove_Employee()
    elif ch == 6:
        system("cls")
        Search_Employee()
    elif ch == 7:
        system("cls")

        print("{:>60}7".format("Have a wonderful day!!)"))
        exit(0)
    else:
        print("Invalid Choice!\nPlease try again.")
        press = input("Press Any key To Continue.")
        menu()

menu()
