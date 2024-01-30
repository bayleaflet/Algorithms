# Stores a collection of unordered unique items. Does not allow duplicate items
# and will return False
# You must override the __eq__operator for any class objects you put in Bag.
# Baylee Christensen
# CS 2420 9/2023

class Bag:
    def __init__(self):
        self.A = []

    def Insert(self,x): # Return false if x is duplicate
        if self.Exists(x):
            return False
        else:
            self.A.append(x)
            return True

    def Exists(self,x):
        for item in self.A:
            if item==x:
                return True
        return False


    def Size(self):
        return len(self.A)

    def __iter__(self):
        for item in self.A:
            yield item

    def Delete(self, dummyStudent):
        if not self.Exists(dummyStudent):
            return False # Can't delete if not there
        for i in range(len(self.A)):
            if self.A[i] == dummyStudent:
                self.A.pop(i)
                break


    def Retrieve(self,x):
        for item in self.A:
            if item==x:
                return item
        return None

