"""
@ brief 判断年份是否为闰年
@ Author Ares
@ Date  2019-10-23

"""

while True:
    year = int(input("请输入年份："))
    result = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)
    if result:
        print("该年份是闰年\r\n")
    else:
        print("该年份是平年\r\n")