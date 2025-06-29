from oop.college import College


class Teacher(College):
    def __init__(self, cname, caddr, noofdept, eid, tname, tdept, tsal):
        super().__init__(cname, caddr, noofdept)
        self.empid = eid
        self.tname = tname
        self.tdept = tdept
        self.sal = tsal

    def display_teacherinfo(self):
        print(f'Emp id : {self.empid} Name : {self.tname} Dept : {self.tdept} salary : {self.sal}')