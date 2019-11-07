"""元组"""

"""tuple不能变了，它也没有append()，insert()这样的方法。
其他获取元素的方法和list是一样的，
你可以正常地使用classmates[0]，
classmates[-1]，但不能赋值成另外的元素。
"""
classmates = ("许广杰","dyy","cdm")
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])

#空元组
emptyTuple = ()
print(emptyTuple)

#一个元素的元组
oneObjTuple = ("EmbeddedXGJ",)
print(oneObjTuple)

changeTuple = ("Dyy","Cdm",["Ares","Xgj"])
changeTuple[2][1] = "AAA"
changeTuple[2][0] = "BBB"
print(changeTuple)