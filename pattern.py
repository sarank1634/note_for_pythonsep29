# rows = 5

# for i in range(1,rows +1):
#     print(" "*(rows-i)+ "*"*(2*i-1))

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = person("dong","fang")
x.printname()
        