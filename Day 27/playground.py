# Unlimited positional arguments
# unlimited arguments   

def add(*args):
    sum = 0
    for x in args: # args akan berbentuk tupple
        sum = sum + x
    return sum

print(add(1,1,1,1,1,2,2,2,3,4,5,6,10))

# Unlimited keywords arguments

def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(key, value)
        
    n = n + kwargs["add"]
    n = n * kwargs["multiply"]
    
    return n

print(calculate(2, add = 3, multiply = 5))