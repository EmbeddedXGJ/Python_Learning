"""
@ brief 英制单位英寸和公制单位厘米互换
@Author Ares
@Date  2019-10-23

"""

while True:
    val = float(input("请输入长度："))
    uint = input("请输入单位：")
    if uint == "in" or uint == "英寸":
        print("%f英寸 = %f厘米" % (val,val * 2.54))
    elif uint == "cm" or uint == "厘米":
        print("%f厘米 = %f英寸" % (val,val / 2.54))
    else:
        print("请输入有效单位\r\n")