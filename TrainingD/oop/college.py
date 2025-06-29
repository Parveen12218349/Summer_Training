class College:
    def __init__(self,cname, caddr, noofdept):
        self.cname = cname
        self.caddr = caddr
        self.no_of_dept = noofdept

    def display_collegeinfo(self):
        print(f'Name :{self.cname} \t Addr :{self.caddr} \t Department count :{self.no_of_dept}')