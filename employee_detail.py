employee = {}
employee['name'] = input("Enter the name of the employee: ")
employee['age'] = int(input("Enter the age of employee: "))
employee['department'] = input("Enter the department of employee: ")
employee['salary'] = float(input("Enter the salary of the employee: "))
employee['experience'] = int(input("Enter the years of experience of the employee: "))
employee['joining_date'] = input("Enter the joining date of the employee (YYYY-MM-DD): ")
employee['email'] = input("Enter the email of the employee: ")
employee['phone_number'] = input("Enter the phone number of the employee: ")
employee['address'] = input("Enter the address of the employee: ")
print ("\n Employee details:")
print("---------------------")
for key, value in employee.items():
    print(key, ":", value)

