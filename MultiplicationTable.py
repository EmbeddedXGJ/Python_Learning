"""
@brief   输出9x9乘法表
@Author  Ares
@Date   2019-10-23

"""

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i * j),end='\t')
    print("\n")