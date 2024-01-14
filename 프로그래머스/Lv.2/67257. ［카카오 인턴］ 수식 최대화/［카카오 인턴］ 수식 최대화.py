"""
-100 * -220 => 22,000

(*, 3), (+, 2), (-, 1)

=> 

"""
import re
from itertools import permutations
from operator import add, sub, mul


def solution(expression):
    answer = 0
    
    tokens = re.findall("[+-/*]|\d+", expression)
    operands = set([token for token in tokens if token in '+-*'])
    op_ranks = []
    
    for comb in permutations(operands, len(operands)):
        rank = {}
        for idx, op in enumerate(comb):
            rank[op] = idx
        op_ranks.append(rank)
        
        
    def to_postfix(expr, op_rank):
        operators = []
        postfix = []
        expression = []
        
        for token in expr:
            if token not in op_rank:
                postfix.append(token)
            else:
                while operators and op_rank[operators[-1]] >= op_rank[token]:
                    postfix.append(operators.pop())
                operators.append(token)
                
        while operators:
            postfix.append(operators.pop())
            
        return postfix
    
    
    def eval(expr, op_rank):
        op = { '+': add, '-': sub, '*': mul }
        stack = []
        
        for token in to_postfix(expr, op_rank):
            if token not in op:
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(op[token](n2, n1))
        
        return abs(stack.pop())
    
    answer = 0
    for rank in op_ranks:
        answer = max(answer, eval(tokens, rank))
    
    return answer