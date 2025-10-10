# rows = 5

# for i in range(1,rows +1):
#     print(" "*(rows-i)+ "*"*(2*i-1))

# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# x = person("dong","fang")
# x.printname()


# class student:
#     def __init__(self, name, age):
#         self.fullname = name
#         self.current_age = age 

# x = student("saran", 26)
# print(x.current_age, x.fullname)
        
# class Person: 
#     def __init__(self, rollno, name, std,grade):
#         self.Rollno = rollno
#         self.fullname = name
#         self.standrd = std 
#         self.grades = grade

# student = Person(121, "saran", 12, "s") 

# print(student.fullname, student.Rollno, student.standrd, student.grades)

# del student.grades

# print(student.fullname, student.Rollno, student.standrd)




class Person:
    def __init__(self,fname, lname):
        self.first_name = fname
        self.last_name = lname

    def printname(self):
       print(self.first_name, self.last_name)

x = Person("ram","kumar")
x.printname()

        