with open('input.txt', 'r') as f:
    lines = f.readlines()
    stripped_lines = [line.rstrip('\n') for line in lines[:-1]]


import operator
from functools import reduce 
from itertools import groupby

# Dictionary mapping strings to operator functions
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

operators = [ops[x] for x in lines[-1].split()]

lists=[line.split() for line in lines[:-1]]
print(sum(reduce(op, map(int,values)) for *values, op in  zip(*lists,operators) ))

columns = [''.join(col) for col in zip(*stripped_lines)]
result = [list(group) for key, group in groupby(columns, key=lambda x: not x.isspace()) if key]

print(sum(reduce(op, map(int,values)) for values, op in  zip(result,operators) ))
