# BJC, Original Author
# 09/30/2023

class Student:

    def __init__(self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    def getAge(self):
        return self.mAge

    def __eq__(self,rhs):
        return self.mSSN == rhs.mSSN
    def __lt__ (self,rhs): # less than
        return self.mSSN < rhs.mSSN
    def __le__(self, rhs): #less than or equal
        return self.mSSN <= rhs.mSSN
    def __gt__(self, rhs): # greater than
        return self.mSSN > rhs.mSSN
    def __ge__(self, rhs): # greater or equal
        return self.mssN >= rhs.mSSN
    def __ne__(self,rhs): # Not equal
       return self.mSSN != rhs.mSSN
