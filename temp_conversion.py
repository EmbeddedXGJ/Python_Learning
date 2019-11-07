"""
@ brief 华氏度转摄氏度
@ Author Ares
@Date    2019-10-23

"""
while True:
    f = float(input("请输入华氏温度："))
    c = (f - 32) / 1.8
    print("%.2f 华氏度 = %.2f摄氏度" % (f,c))