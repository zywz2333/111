'''
设计一个红绿灯的程序，按顺序和时间输出红绿灯的颜色，peint("红灯“)这种效果
红灯，绿灯，黄灯
'''

'''
包的引用

包-->模块-->类-->方法-->变量

'''

'''
# import time  # 直接导入整个包
from time import sleep  # 只导入了time这个包里面的sleep方法


# sss = time.strftime("%Y-%m-%d %H:%M:%S")


light = {
    "红灯":30,
    "绿灯":30,
    "黄灯":3
}
while True:  # 死循环
    for i in light:
        t = light.get(i)
        while t != 0:
            print("{}倒计时{}秒".format(i,t))
            sleep(1)
            t = t - 1


'''

'''
判断今天是今年的第几天？
闰年直接理解为满足以下两个条件之一，即是闰年： 
1、年份能被4整除，且不能被100整除 
2、年份能被400整除

2019年7月24号
确认2019年是平年还是闰年
[31,28,31,30,31,30,31,31,30,31,30,31]
31+28+31+30+31+30+24
'''

htsr = input("请输入今天的日期，格式如2019-7-24：")
xxx = htsr.split("-")
newymd = []
for i in xxx:
    i = int(i)
    newymd.append(i)
year = newymd[0]
month = newymd[1]
day = newymd[2]

mlist = [31,28,31,30,31,30,31,31,30,31,30,31]  # 月份的数组
days = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    mlist[1] = 29
    for i in range(month-1):
        days = days + mlist[i]
    days = days + day
else:
    for i in range(month-1):
        days = days + mlist[i]
    days = days + day
print("今天是{}年的第{}天".format(year,days))

