class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, name):
        return f"I love {name}"