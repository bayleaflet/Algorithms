import math


def IsPrime(x):
    if x == 2:
        return True
    s = round(math.sqrt(x))
    for i in range (2, s+1):
        if x%i ==0:
            return False
    return True

class Hash:
    def __init__(self, numItems): # Will need to adjust numItem later
        # Creates table full of Nones the size of prime number above (numItems *2)
        self.tableSize = numItems *2 +1
        while not IsPrime(self.tableSize):
            self.tableSize += 2
        self.table = [None] * self.tableSize
        self.count = 0 # Need to mod this so that it's easier to count.

    def __iter__(self):
        for i in range(self.tableSize):
            if self.table[i]:
                yield self.table[i] # The i might need to be a 1

    def Size(self):
        return self.count

    def Exists(self, item):
        key = hash(item)
        index = key % self.tableSize
        while True:
            if self.table[index] is None:
                return False
            elif self.table[index] and self.table[index] == item:
                return True
            else:
                index +=1
                if index >= self.tableSize:
                    index = 0

    def Retrieve(self, item):
        key = hash(item)
        index = key % self.tableSize

        while True:
            if self.table[index] is None:
                return None  # Item not found
            elif self.table[index] == item:
                return self.table[index]  # Item found
            else:
                index += 1
                if index >= self.tableSize:
                    index = 0

        # Additional check to avoid an infinite loop if the table is full
            if index == key % self.tableSize:
                return None  # Item not found (avoid infinite loop)
    '''
    def Retrieve(self, item):
        if not self.Exists(item):
            return None
        key = hash(item)
        index = key % self.tableSize
        while True:
            if self.table[index] and self.table[index] == item:
                return self.table[index]
            else:
                index +=1
                if index >= self.tableSize:
                    index = 0
    '''
    def Delete(self, item):
        if not self.Exists(item):
            return False
        key = hash(item)
        index = key% self.tableSize
        while True:
            if self.table[index] and self.table[index] == item:
                self.table[index] = None
                self.count -= 1
                return True
            index +=1
            if index >= self.tableSize: #wraps around to keep searching
                index = 0

    def Insert(self, item):
        key = hash(item)
        index = key% self.tableSize
        if self.count / self.tableSize > 0.5:
            self.resize_table()

        if self.Exists(item):
            return False
        i = 1
        while self.table[index]:
            if self.Exists(item):
                return False
            h2 = self.secondary_hash_function(key)
            index = (index +i *h2) % self.tableSize
            i +=1
        self.table[index] = item
        self.count += 1
        return True

    def secondary_hash_function(self, key):
        prime = 31
        h2 = prime - (key % prime)
        return h2

    def resize_table(self):
        # Double the size of the table and rehash all elements
        new_size = self.tableSize * 2 + 1
        while not IsPrime(new_size):
            new_size += 2

        new_table = [None] * new_size

        # Rehash all elements into the new table
        for item in self.table:
            if item is not None:
                key = hash(item)
                new_index = key % new_size
                new_table[new_index] = item

        self.table = new_table
        self.tableSize = new_size
