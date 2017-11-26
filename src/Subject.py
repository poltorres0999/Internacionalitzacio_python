import gettext



class Subject :
    def __init__(self, Name, ID, Credits):
        self.Name = Name
        self.ID = ID
        self.Credits = Credits
        pass

    def printSubject(self):
        print(_("Subject name: "), self.Name + '\n')
        print(_("Subject ID: "), self.ID + '\n')
        print(_("Number of credits: "), self.Credits + '\n')