def add(*args):
    sum = 0
    for x in args: # args akan berbentuk tupple
        sum = sum + x
    return sum

print(add(1,1,1,1,1,2,2,2,3,4,5,6,10))
    