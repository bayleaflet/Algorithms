# Linked List
# BJC, original author. 10/2023

class Node:
    def __init__(self, item, n):
        self.mItem = item
        self.mNext = n

class Bag:
    def __init__(self):
       self.mFirst = None


    def Insert(self, item):
        new_node = Node(item, None)
        # if self,exist(item):
        # return False
        if not self.mFirst:
            self.mFirst = new_node
        else:
            current = self.mFirst
            while current.mNext:
                current = current.mNext
            current.mNext = new_node

    def Exists(self,item):
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def Size(self):
        counter = 0
        current = self.mFirst
        while current is not None:
            counter += 1
            current = current.mNext
        return counter

    def Retrieve(self,item):
        # what if object is empty?
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return None

    def __iter__(self):
        current = self.mFirst
        while current is not None:
            yield current.mItem
            current = current.mNext

    def Delete(self, dummyStudent):
        current = self.mFirst
        previous = None
        while current is not None:
            if current.mItem == dummyStudent:
                if previous is not None:
                    previous.mNext = current.mNext
                else:
                    self.mFirst = current.mNext
                return True
            previous = current
            current = current.mNext
        return False

