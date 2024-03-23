from sys import stdin


expr = stdin.readline()
operators = []

priority = {
    "(": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1
}
ret = ''

for ch in expr:
    if ch.isalpha():
        ret += ch
        
    elif ch in ["*", "/", "+", "-"]:
        while operators \
            and operators[-1] != '('\
            and priority[operators[-1]] >= priority[ch]:
            ret += operators.pop()
        operators.append(ch)
        
    elif ch == '(':
        operators.append(ch)
    elif ch == ')':
        while operators and operators[-1] != '(':
            ret += operators.pop()
        operators.pop()

while operators:
    ret += operators.pop()
    
print(ret)