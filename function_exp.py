from random import  randint

def myFactorial(num):
    """求阶乘"""
    result = 1
    for n in range(1,num + 1):
        result *= n

    return result


# m = int(input("m = "))
# n = int(input("n = "))
#endResult = myFactorial(m) // myFactorial(n) // myFactorial(m - n)
#print(endResult)

def roll_dice(n = 2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return  total

def myAdd(a=0,b=0,c=0):
    return a + b + c


print(roll_dice())
print(roll_dice(3))
print("\r\n")

print(myAdd())
print(myAdd(1))
print(myAdd(1,2))
print(myAdd(1,2,3))

# 传递参数时可以不按照设定的顺序进行传递
print(myAdd(c = 200,a = 100,b = 0))

print("\r\n")

print("可变参数例子")
def variable_add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(variable_add())
print(variable_add(1))
print(variable_add(1,2))
print(variable_add(1,2,3))
print(variable_add(1,3,5,7,9))