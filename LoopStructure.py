"""
    循环结构
"""

###求1+2+3+...+99+100的和
sum = 0
for x in range(101):
    sum += x
print("1~100和 = %d" % sum)


###求1~100之间的偶数和
sum1 = 0
for y in range(2,100,2):
    sum1 += y
print("1~100偶数和 = %d" % sum1,"\r\n")

import  random

answer = random.randint(1,100)
count = 0
while True:
    count += 1
    number = int(input("请输入猜的数字："))
    if number < answer:
        print("提示：大一点")
    elif number > answer:
        print("提示：小一点")
    else:
        print("恭喜你猜对了\r\n")
        break
print("你总共才了%d次" % count)
if count > 7:
    print('明显你的脑袋被门挤了\r\n')
