class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.number = 0

    def return_occupation(self):
        return self.occupation

class Teacher(Person):
    def __init__(self, name, occupation, subject):
        super().__init__(name, occupation)
        self.subject = subject

person = Person("Larry", "Student")
teacher = Teacher("amy", "teacher", "chinese")
print(teacher.number)