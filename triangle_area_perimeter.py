"""
@brief 判断输入边长能否构成三角形，能则计算三角形周长和面积
@Author Ares
@Date   2019-10-23

"""

while True:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("是三角形\n")
        print("周长：",a + b + c)
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("面积：",area)
    else:
        print("输入边长不能构成三角形\r\n")