```.py
class Employee:
    def __init__(this_employee, username, email, age, salary, role):
        this_employee.name = username
        this_employee.role = role
        this_employee.email = email
        this_employee.age = age
        this_employee.salary = salary

    def greet(this_employee):
        name = this_employee.name
        email = this_employee.email
        role = this_employee.role
        age = this_employee.age
        salary = this_employee.salary
        return (f"Hello {name.title()}, you are {age} years old and work as a {role} in our company. \
        Your email address is {email}.")

    def email_adress(this_employee):
        name = this_employee.name
        email = this_employee.email
        return (f"{email} is {name}'s email address.")


emp_1 = Employee(username="Shahru Shabanov", email="shabanovshahru.de@gmail.com", role="shop assistant", age=22,
                 salary=8400)
emp_2 = Employee(username="Lison Hebert", email="2024.lison.fenghan.hebert@uwcisak.jp", role="drop shipper", age=17,
                 salary=20000)

database = [emp_1, emp_2]

for emp in database:
    print(emp.email_adress())
```
