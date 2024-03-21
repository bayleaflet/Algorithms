class Node:
    def __init__(self, item):
        self.mItem = item
        self.mLHS = None
        self.mRHS = None

class BST:
    def __init__(self):
        self.mRoot = None
        self.count = 0 # WHen adding a item or subtractin,g do + or minus
    def __iter__(self):
        yield from self.IterR(self.mRoot)

    def IterR(self,current):
        if current is not None:
            yield from self.IterR(current.mLHS)
            yield current.mItem # onlly yields to layer right above it
            yield from self.IterR(current.mRHS)
    def Insert(self, item):
        if self.Exists(item):
            return False # Not adding duplicate
        n = Node(item)
        self.mRoot = self.InsertR(n, self.mRoot) #Insert recursively
        self.count += 1
        return True

    def InsertR(self, n, current):
        if current is None:
            current = n # current points to same node n is pointing to
        elif n.mItem< current.mItem:
            current.mLHS = self.InsertR(n, current.mLHS) # parent sets pointer to
        else: # Go down current's right side
            current.mRHS = self.InsertR(n, current.mRHS)
        return current # Returns current back to parent

    def Exists(self, item):
        return self.ExistsR(item, self.mRoot)

    def ExistsR(self, item, current):
        if current is None:
            return False
        elif item == current.mItem:
            return True
        elif item < current.mItem:
            return self.ExistsR(item, current.mLHS)
        elif item > current.mItem:
            return self.ExistsR(item, current.mRHS)

    def Retrieve(self, item):
        if not self.Exists(item):
            return None
        return self.RetrieveR(item,self.mRoot)
    def RetrieveR(self, item, current):
        #Trying out this new method
        if item < current.mItem:
            return self.RetrieveR(item, current.mLHS)
        elif item > current.mItem:
            return self.RetrieveR(item, current.mRHS)
        else:
            return current.mItem


    def Size(self):
        return self.count

    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.mRoot = self.DeleteR(item, self.mRoot)
        self.count -= 1

    def DeleteR(self, item, current):
        if item < current.mItem:
            current.mLHS = self.DeleteR(item, current.mLHS)
        elif item > current.mItem:
            current.mRHS = self.DeleteR(item, current.mRHS)
        else:
            if current.mLHS is None:
                return current.mRHS
            elif current.mRHS is None:
                return current.mLHS
            successor = self.FindSuccessor(current.mRHS)
            current.mItem = successor.mItem
            current.mRHS = self.DeleteR(successor.mItem, current.mRHS)
        return current

    def FindSuccessor(self, node):
        while node.mLHS:
            node = node.mLHS
        return node


