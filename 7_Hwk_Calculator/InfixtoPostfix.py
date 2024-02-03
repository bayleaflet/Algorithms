#BJC, Original Author
# 10/2023
# Converts infix to postfix
from stack import Stack
# Code is supposed to set * and / as "A" priority, while +- are "B"
# priority. Only items with "A" priority can go on top of those with "B"
# priority. However if the priority is equal, the stack must be completely
# pushed to postfix. Parenthesis are used as dividers for each evaluation, and
# if a parenthesis is in the expression, the stack is considered brand new.
# Once the right parentheses is encountered, everything on top of the left
# parenthesis is pushed to postfix.

#Working correctly!
def InfixtoPostfix(infix):
    postfix = ""
    s = Stack()
    for c in infix:
        if c in "0123456789x": # Is it a digit or is x?
            postfix += c
        elif c in "*/":
            while not s.isEmpty() and s.top() in "*/":
                postfix += s.pop()
            s.push(c)
        elif c in "+-":
            while not s.isEmpty() and s.top() in "*/+-":
                postfix += s.pop()
            s.push(c)
        elif c == ")":
            while not s.isEmpty() and s.top() != '(':
                postfix += s.pop()
            s.pop() # Removes the left parent
        elif c == "(":
            s.push(c)

    while not s.isEmpty():
        postfix += s.pop()

    return postfix


def EvaluatePostFix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in "0123456789":
            s.push(float(c))
        elif c == 'x':
            s.push(x)
        elif c == '+':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs + rhs
            s.push(result)
        elif c == '-':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs - rhs
            s.push(result)
        elif c == '/':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs / rhs
            s.push(result)
        elif c == "*":
            rhs = s.pop()
            lhs = s.pop()
            result = lhs * rhs
            s.push(result)
    answer = s.pop()
    return answer
