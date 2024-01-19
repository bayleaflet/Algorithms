class Student:
    def __init__(self, last, first, ssn, email, age):
        self.mLast = last
        self.mfirst = first
        self.ssn = ssn
        self.email = email
        self.age = age

    def __eq__(self, rhs):
        return self.ssn == rhs.ssn

