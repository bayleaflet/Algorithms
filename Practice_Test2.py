# Practice for Exam 2
def InfixtoPostfix(infix):
    postfix = ''
    s = Stack()
    for c in infix:
        if c in "0123456789x":
            postfix += c
        elif c in "*/":
            while not s.IsEmpty and s.top() in "*/":
                postfix += s.pop()
            s.push(c)
        elif c in "+-":
            while not s.IsEmpty and s.top() in "+-/*":
                postfix += s.pop()
            s.push()
        elif c == "(": #Careful with the parentheses. Needs work
            s.push(c)
        elif c == ")":
            while not s.Isempty and s.top != "(":
                postfix += s.pop()
            s.pop()
    while not s.isEmpty():
        postfix += s.pop()
    return postfix


def EvaluatePostfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in "0123456789":
            s.push(float(c))
        elif c == 'x':
            s.push(x)
        elif c == "+":
            rhs = s.pop()
            lhs = s.pop()
            result =lhs + rhs
            s.push(result)


# methods for linked list
def Insert(self, item):
    new_node = Node(item,None)
    if not self.mFirst:
        self.mFirst = new_node
    else:
        current = self.mFirst
        while current.mNext:
            current = current.mNext
        current.mNext = new_node

def Exists(self, item):
    current = self.mFirst
    while current is not None:
        if current.mItem == item:
            return True
        current = current.mNext
    return False

def Size(self):
    current  = self.mFirst
    while current is not None:
        counter +=1
        current = current.mNext
    return counter

def Retrieve (self, item):
    current = self.mFirst:
        while current is not None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return None

def InfixtoPostfix(infix):
    postfix = ''
    s = Stack()
    for c in infix:
        if c in "num list,x":
            postfix +=c
        elif c in "*/":
            while not s.IsEmpty() and s.top() in "*/":
                postfix += s.pop()
            s.push(c)
        elif c in "+-":
            while not s.IsEmpty() and s.top() in "*/-+":
                postfix += s.pop()
            s.push(c)
        elif c == "(":
            s.push(c)
        elif c == ")":
            while not s.IsEmpty() and s.top() != "(":
                postfix += s.pop()
            s.pop()

    while not s.IsEmpty()
    postfix += s.pop()

def EvalutatePostfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in "0123456789":
            s.push(float(c))
        elif c == "x":
            s.push(c)
        elif c == "+":
            rhs = s.pop()
            lhs = s.pop()
            result = lhs + rhs
            s.push(result)

def Insert(self, item):
    new_node = Node(item, None)
    if not self.mFirst:
        self.mFirst = new_node
    else:
        current = self.mFirst
        while current.mNext:
            current = current.mNext
        current.mNext = new_node


def Exists(self, item):
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
        counter +=1
        current = current.mNext
    return coutner

def Retrieve(self):
    current = self.mFirst
    while current is not None:
        if current.mItem == item:
            return current.mItem
        current = current.mNext
    return None


def Insert(self, item):
    new_node = Node(item, None)
    if not self.mFirst:
        self.mFirst = new_node
    else:
        current = self.mFirst
        while current.mNext:
            current = current.mNext
        current.mNext = new_node


