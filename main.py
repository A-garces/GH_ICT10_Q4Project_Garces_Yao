# Object-oriented programming
from pyscript import display, document

def student_info(e):
    class Student:
        def __init__(self, name, section, subject):
            self.name = name
            self.section = section
            self.subject = subject

        def introduce(self):
            return f'{self.name} is in Section {self.section} and likes to study {self.subject}.'

    output = document.getElementById("output")
    output.innerHTML = ""

    Yao = Student('Franchesca Yao', 'Sapphire', 'Social Studies')
    Kelsey = Student('Kelsey Medina', 'Sapphire', 'Science')
    Alijah = Student('Alijah Lagman', 'Sapphire', 'Math')
    Harvey = Student('Harvey Dolor', 'Sapphire', 'English')
    
    classmates = [Yao, Kelsey, Alijah, Harvey]

    for student in classmates:
        display(student.introduce(), target='output')

def student1_info(e):
    class Student:
        def __init__(self, name, section, subject):
            self.name = name
            self.section = section
            self.subject = subject

        def introduce(self):
            return f'{self.name} is in Section {self.section} and likes to study {self.subject}.'

    output = document.getElementById("output1")
    output.innerHTML = ""
        
    name = document.getElementById("Input1").value
    section = document.getElementById("Input2").value
    subject = document.getElementById("Input3").value

    classmate = Student(name, section, subject)

    User = [classmate]

    for student1 in User :
        display(student1.introduce(), target='output1')
