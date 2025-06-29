from  oop.elective import Elective
from oop.teachers import Teacher

cnm = input('College Name ')

dpmnt = input('Department ')
rno = int(input('Roll No.'))
cad = input('College Address ')
snm = input('Student Name ')
sdpmnt = input('Department ')
Phon = int(input('Phone No.'))
m1 = int(input('Mark 1 '))
m2 = int(input('Mark 2 '))
m3 = int(input('Mark 3 '))
e1 = int(input('Elective 1 '))
e2 = int(input('Elective 2 '))
eid = int(input('Emp id '))
tnm = input('Teacher Name ')
tdpmnt = input('Teacher department ')
sal = int(input('Salary '))


# stud = Student(cnm, cad, rno=rno,  noofdept=dpmnt, sname=snm, sdept=sdpmnt, sph=Phon, m1=m1, m2=m2,m3=m3)

stud = Elective(cname=cnm, caddr=cad, rno=rno,  noofdept=dpmnt, sname=snm,
                sdept=sdpmnt, sph=Phon, m1=m1, m2=m2, m3=m3, e1=e1, e2=e2)

stud.display_collegeinfo()
stud.calc_avg()

print(f'Stu Rno. :{stud.rollno} Name :{stud.sname} Dept :{stud.sdept} '
      f'Average Score :{stud.calc_avg()}')

teacher = Teacher(cname=cnm, caddr=cad,  noofdept=dpmnt, eid=eid, tname=tnm, tdept=tdpmnt, tsal=sal)
teacher.display_teacherinfo()