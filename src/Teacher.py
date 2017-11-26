from src.Person import Person
import gettext


class Teacher(Person):
    def __init__(self, name, surname1, surname2, address, ID, Salary, Subjects):
        super().__init__(name, surname1, surname2, address, ID)
        self.Salary = Salary
        self.Subjects = Subjects

    def printTeacher(self):
        self.print_person()
        print(_('Salary: '), self.Salary + '\n')

        for Subject in self.Subjects:
            Subject.printSubject()