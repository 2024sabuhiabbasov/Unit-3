# Quiz 036

![image](https://user-images.githubusercontent.com/111758436/213425913-97a1bd34-af0a-4e4b-ab56-90f0fc013f87.png)

## My code
```.py
# Program for Quiz 036

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student: Student):
        if student not in self.students:
            raise ValueError("Class is empty")
        self.students.remove(student)

    def get_average_score(self):
        if len(self.students) == 0:
            raise ValueError("Classroom is empty")
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total / len(self.students)
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/216808649-598c7e79-d0b7-4ab2-b04c-98f0aca1a7fa.png)
