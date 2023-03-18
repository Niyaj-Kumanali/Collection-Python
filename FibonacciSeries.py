# #Function that return a list of fibonacci series upto limit
def Fib_limit(end):
    c = []
    a = 0
    b = 1
    if end == 0:
        return end
    c.append(a)
    c.append(b)
    for i in range(end):
        next = a + b
        if end < next:
            break
        c.append(next)
        a, b = b, next
    return c


print(Fib_limit(4181))


# Function that return a list of fibonacci series for given no of times

def Fib_count(n):
    c = []
    a= 0
    b = 1
    if n == 0 or n == 1:
        c.append(0)
        return c
    c.append(a)
    c.append(b)
    if n == 2: return c
    for i in range(n-2):
        next = a + b
        c.append(next)
        a,b = b, next
    return c


print(Fib_count(20))



