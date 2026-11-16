def add_employee(name,id,salary):
    file = open("employees.txt","a")
    file.write(f"{name} | {id} | {salary}\n")
    file.close()

    print("Employee Added Successfully")

def view_employees():
    try:
        file = open("employees.txt","r")
        info = file.read()
        file.close()

        return info
    
    except FileNotFoundError:
        return ""

def employee_details():
    while True:
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            id = input("Enter ID: ")
            salary = int(input("Enter Salary: "))

            add_employee(name,id,salary)

        elif choice == "2":
            info = view_employees()
            
            if info:
                print(info)

            else:
                print("No Employee Record Found!")

        elif choice == "3":
            print("Program Exited Successfully")
            break

        else:
            print("Invalid Option! Try again.")

employee_details()
