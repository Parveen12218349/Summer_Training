from oop.student import Student

class Elective(Student):
    def __init__(self,cname,caddr,noofdept,rno,sname,sdept,sph,m1,m2,m3,e1,e2):
        super().__init__(cname,caddr,noofdept,rno,sname,sdept,sph,m1,m2,m3) ## self ><
        self.elec1 = e1
        self.elec2 = e2

    def calc_total(self):
        return self.mark1 + self.mark2 + self.mark3 + self.elec1 + self.elec2

    def calc_avg(self):
        return self.calc_total() / 5