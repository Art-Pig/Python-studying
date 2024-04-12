# 求三角形面积程序
#   班级：22电子1班
#   学号：22180210
#   姓名：王泽万
#

print("请分别输入三角形的三条边长")
print("请注意：两边之和要大于第三边，两边之差要小于第三边！")

flag = True  #作为while循环判断标志

x = 0   #三条边初始化

y = 0

z = 0

while(flag):    #循环输入，直至输入正确
    x = eval(input('第一条边X：'))

    y = eval(input('第二条边Y：'))

    z = eval(input('第三条边Z：'))

    if (x+y<z)|((x-y if x-y > 0 else y-x)>z):   #判断三边是否符号三角形定义

        print("输入数据有误，请重新输入！")

    elif (x+z<y)|((x-z if x-z > 0 else z-x)>y):

        print("输入数据有误，请重新输入！")

    elif (y+z<x)|((y-z if y-z > 0 else z-y)>x):

        print("输入数据有误，请重新输入！")

    elif x==0|y==0|z==0:

        print("输入数据有误，请重新输入！")

    else:

        print("输入数据有效！")

        flag = False    # 输入有效则循环结束

q = float((x+y+z)/2)

S = float((q*(q-x)*(q-y)*(q-z))**0.5)   #三角形面积公式

print("您输入的三角形的面积为：{}".format(S))  #输出结果





