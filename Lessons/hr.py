emp_1 = ["Shahru Shabanov", "shabanovshahru.de@gmail.com", "shop assistant", 22, 8400]
emp_2 = ["Lison Hebert", "2024.lison.fenghan.hebert@uwcisak.jp", "drop shipper", 17, 20000]
emp_3 = ["Ibrahim Mammadov", "imammadov@college.harvard.edu", "web developer", 21, 45000]

database = [emp_1, emp_2, emp_3]

def greet(emp: list) -> str:
    name = emp[0]
    email = emp[1]
    role = emp[2]
    age = emp[3]
    return (f"Hello {name.title()}, you are {age} years old and work as a {role} in our company. Your email address is {emp[1]}.")

for i in (0, 2):
    print(greet(database[i]))
