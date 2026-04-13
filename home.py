emp_ids = [101,102,103]
emp_names = ["Arun","Bala","Chitra"]
emp_salary = [20000,25000,30000]

print("A - Add")
print("E - Edit")
print("D - Delete")
print("V - View")

choice = input("Enter choice: ").upper()

# ADD
if choice == "A":
    new_id = int(input("Enter ID: "))
    new_name = input("Enter Name: ")
    new_salary = int(input("Enter Salary: "))

    emp_ids.append(new_id)
    emp_names.append(new_name)
    emp_salary.append(new_salary)

    print("Employee Added")

# EDIT
elif choice == "E":
    edit_id = int(input("Enter ID to edit: "))

    if edit_id in emp_ids:
        index = emp_ids.index(edit_id)
        emp_names[index] = input("Enter New Name: ")
        emp_salary[index] = int(input("Enter New Salary: "))
        print("Employee Updated")
    else:
        print("Employee Not Found")

# DELETE
elif choice == "D":
    delete_id = int(input("Enter ID to delete: "))

    if delete_id in emp_ids:
        index = emp_ids.index(delete_id)
        emp_ids.pop(index)
        emp_names.pop(index)
        emp_salary.pop(index)
        print("Employee Deleted")
    else:
        print("Employee Not Found")

# VIEW
elif choice == "V":
    for i in range(len(emp_ids)):
        print(emp_ids[i], emp_names[i], emp_salary[i])

else:
    print("Invalid Choice")
