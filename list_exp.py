
""" 列表 """

myList = ["I am you fathe!","I am your dad!","我是你爸爸"]
myList = myList + ["you are my son","you are my daughter"]  #在列表最后插入 ["you are my son","you are my daughter"]

print(myList)

print(myList[1])

myList.append("hello world")  #在列表最后插入hello world
print(myList[-1])

myList.insert(2,"fuck you DengCuifang")  #将"fuck you DengCuifang"插入到索引号为2的列表项中
print(myList[2])

print(myList)

myList.pop()  #删除列表最后一个元素
print(myList)



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])

# 打印Python:
print(L[1][1])

# 打印Lisa:
print(L[2][2])

"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""
"""
体质指数（BMI）=体重（kg）÷ 身高²（m）
"""
height = float(input("身高："))
weight = float(input("体重："))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("过轻")
elif BMI >=18.5 and BMI < 25:
    print("正常")
elif BMI >= 25 and BMI < 28:
    print("过重")
elif BMI >= 28 and BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")

