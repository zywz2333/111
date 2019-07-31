# 面向对象：只要是用到了类，我们就可以理解为面向对象编程；
# 通过发送指令的方式来调用对应的功能就行了，手机打电话，我们需要打电话的时候就直接去引用打电话的功能就行了
#class Phone:
#    band = "苹果"
#    price = 8888
aaa = 111

#====== 一、知道类的定义，成员变量的定义 成员方法的定义，以及怎么实例化这个类，怎么去获取成员变量、成员方法

# class：关键字，去告诉python，我要去定义一个类
# Person：类的名字，关键字和类名中间是有一个空格的，命名首字母要大写
#           如果类名是由两个单词组成的，那就这两个单词的首字母都大写 class NoteBookComputer
# ()：可写可不写，如果这个类要去继承另外的类，那么就需要
class Person():
    # 类的成员变量
    username = "羊羊羊"
    age = 18
    heigth = 188
    weight = 50

    # 类的功能：成员方法，必须以self关键字为第一个参数
    # 类同样的行为就理解为功能
    def run(self):
        # 1. 穿鞋子
        # 2. 穿裤子
        # 3. 开门
        # 4. 裸奔
        print("人类可以跑！")
    def eat(self):
        print("人类可以吃饭")

# 类的实例化
yanghaonan = Person()
# 获取类的成员变量
print(yanghaonan.username)
yanghaonan.run()


# ============================ 二、难一点点点点点点点的内容
# 1. 类里面的成员方法是怎么传参的呢
# 2. self这个关键字的含义 self就是这个类的实例化对象本身，实例化对象p是在用类外面的，self是用在类里面的

class Phone():
    band = "华为"
    color = "蓝色"
    price = 6888

    def call(self, telnum):
        print("正在拨打号码{}".format(telnum))

    # 成员方法去引用成员变量
    def decript1(self):
        print("这是一台价值{}的{}{}的手机".format(self.price, self.color, self.band))
    
    # 成员方法调成员方法
    def descript2(self):
        self.decript1()

p = Phone()
p.call("110")
p.decript1()
p.descript2()

# ========================== 三、难那么一丢丢的: 记住
# 1. 类的构造方法：在实例化这个类的时候，我们可以通过构造方法来初始化这个类的一些事情
class FanWan():
    chang = "10cm"
    kuan = "10cm"
    mingzi = "小白"
    yanse = "白色"

    # 构造方法，需要传递 长、宽、名字、颜色这个四个变量
    def __init__(self, c, k, mz, ys):
        self.chang = c
        self.kuan = k
        self.mingzi = mz
        self.yanse = ys
        self.zhaugnfan()

    def zhaugnfan(self):
        print("我能乘饭")

wan = FanWan("20cm", "20cm", "小黑", "黑色")
print(wan.chang)
print(wan.kuan)
print(wan.mingzi)
print(wan.yanse)

# 2. 类的继承：继承最大的好处是子类获得了父类的全部功能，包括变量和方法
# QingHuaCi是Wan的子类
# Wan是QingHuaCi的父类
class Wan():
    name = "金箔"
    def huayuan(self):
        print("唐三藏的金箔可以化缘")

class QingHuaCi(Wan):
    # 重写父类的成员变量
    name = "青花瓷器碗"

    # 重写父类的方法
    def huayuan(self):
        print("我是青花瓷了，不需要化缘！")

qhc = QingHuaCi()
print(qhc.name)
qhc.huayuan()




