'''
jine = input("请输入金额：")  # 获取输入金额，赋值给jine这个变量
print("输入的金额为：",jine)   # 打印jine

num = jine.count(".")  #  统计jine这个字符串中，有多少个小数点
if num == 0 or num == 1:  # 判断小数的个数，只有小数点为0或者为1个的情况，才认为是正常的数字
    hstr = "0123456789."  # 199.99
    for i in jine:
        if i not in hstr:  # 判断jine这个字符串中，是否存在非数字和小数点的值
            print("输入的值不合法，请输入数字！")
            exit()  # 退出程序
    jine = float(jine)  # 强制转换数据类型为float
    if jine >= 0.01 and jine <= 200:
        print("发送红包成功！")
    else:
        print("金额超出范围！")
else:
    print("输入的金额不合法，只能输入数字！")

'''


for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")
    print()

name = "张三"
age = 23
print("你好！我的名字叫{name}，我今年{age}岁！{name}喜欢吃胡萝卜！".format(name=name,age=age))

num = 1
while num < 10:
    print("这是第{}次循环".format(num))
    num = num + 1

print("--------------------------------")


for i in range(9):
    print("这是第{}次循环".format(i))



# age = int(input("请输入你的年龄："))
age = 13

if age < 6:
    print("你还是一个孩子啊！")
elif age < 12:
    print("你已经开始上小学啦！")
elif age < 18:
    print("你可以开始早恋了孩子！")
elif age < 24:
    print("这个时候你还没对象，你这个单身狗！")
else:
    print("是时候成家立业了！")



'''
有这样子的一个数组，[78,76,56,99,100,76,64,45,67,87,75,56,90,90,87,65]
通过代码，将这个数组，以【60】为分割线，拆分成2个不同的数组，并打印输出！
'''
hlist = [78,76,56,99,100,76,64,45,67,87,75,56,90,90,87,65]
highlist = []
lowlist = []
for i in hlist:
    if i >= 60:
        highlist.append(i)
    else:
        lowlist.append(i)
print("大于60的数组：",highlist)
print("小于60的数组：",lowlist)





