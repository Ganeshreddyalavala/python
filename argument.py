#positional-perameters AND default perameters
'''def dispstudent(stno,sname,marks):
    print("\t{}\t{}\t{}".format(stno,sname,marks,"""course"""))
    
dispstudent(10,"Ganesh",34.56)
dispstudent(20,"HUDSAN",56.65)
dispstudent(30,"DETTOL",99.99)'''

"""def dispempinfo(eno,ename,sal,des):
    print("\t{}\t{}\t{}\t{}".format(eno,ename,sal,des))

dispempinfo(111,"RS",5.6,"TL")
dispempinfo(des="HR",sal=6.0,ename="TG",eno=117)"""

#keyword variabel length perameter
def totalmarks(sname,cls, **infor):
 print("Student Name:{}".format(sname))
 print("Student Studying in :{}".format(cls))
 print("\tSubjects\tMarks")
 totmarks=0
 for subj,marks in infor.items():
     print("\t{}\t\t{}".format(subj,marks))
     totmarks=totmarks+marks
 else:
     print("\tTotalMarks={}".format(totmarks))
     
#main block
totalmarks("ganesh",10,ENG=75,CHE=25)
totalmarks("harish",12,tel=95,hin=45)

#variablelengthparameter








