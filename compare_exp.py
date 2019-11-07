"""
@ brief  比较逻辑运算符的使用
@ Author Ares
@ Date   2019-10-23

"""

a = 3
b = 5
c = 3

ret1 = a > b
ret2 = a == c
ret3 = b > c

ret4 = ret1 and ret3
ret5 = ret1 or ret2
ret6 = not ret1

print("ret1 = ",ret1,"\r\n")
print("ret2 = ",ret2,"\r\n")
print("ret3 = ",ret3,"\r\n")
print("ret4 = ",ret4,"\r\n")
print("ret5 = ",ret5,"\r\n")
print("ret6 = ",ret6,"\r\n")

