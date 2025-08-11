def area(x):
    return x[0] * x[1]

p = [(3,3), (4,2), (2,2), (5,2), (1,7)]

q1 = sorted( p, key = area)
print(q1)

q2 = sorted(p, key = lambda x: x[0]* x[1])
print(q2)