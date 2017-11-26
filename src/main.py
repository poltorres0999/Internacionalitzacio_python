import gettext


from src.Student import Student
from src.Subject import Subject
from src.Person import Person
from src.Teacher import Teacher

if __name__ == '__main__':

    gettext.install(domain='main', localedir='locales')

    p1 = Person('pol', 'torres','alfonso','calleFalsa','482594591')

    subjects = [Subject('maths', '1', '9'), Subject('biology', '11', '9'), Subject('physics', '13', '9')]

    s1 = Student('pol', 'torres','alfonso','calleFalsa','482594591','15','4',subjects)
    t1 = Teacher('pol', 'torres', 'alfonso', 'calleFalsa', '482594591', '999', subjects)

    p1.print_person()
    t1.printTeacher()
    s1.print_student()