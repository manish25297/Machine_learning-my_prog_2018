student=[]                               #list
name={}
stu={}                                   #dictionary
for i in range(3):
    a=raw_input("enter ur name")
    b=raw_input("enter the roll no. ")
    name={a:b}                          
    stu.update(name)                     #stu[a]=b updating dictionary
    student.append(name)                 # appending list or this can be done #stu[a]=b
    print student
    print stu
