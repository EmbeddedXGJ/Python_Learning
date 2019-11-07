"""
@brief 将成绩换算成等级
@Author Ares
@Date  2019-10-23

"""

while True:
    score = int(input("请输入成绩："))
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "E"

    print("成绩等级：",grade)