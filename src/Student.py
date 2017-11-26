from src.Person import Person

class Student(Person):
    def __init__(self, name, surname1, surname2, address, ID, FNumber, Course, Subjects):
        super().__init__(name, surname1, surname2, address, ID)
        self.FNumber = FNumber
        self.Course = Course
        self.Subjects = Subjects
        pass

    def print_student(self):
        self.print_person()
        print(_('File Number: '), self.FNumber + '\n')
        print(_('Course: '), self.Course + '\n')

        for Subject in self.Subjects :
            Subject.printSubject()