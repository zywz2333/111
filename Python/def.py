
a = "yyy"

def testxxx():
    x = "sss"
    print(a)
# 在外面引用是不行的
#  print(x)

testxxx()


# 面向过程：只需要去关心实现的过程
def add(x, y):
    sum = x + y
    return sum

#a = add(1, 2)
# print(a)

# 面向对象：只要是用到了类，我们就可以理解为面向对象编程；
# 通过发送指令的方式来调用对应的功能就行了，手机打电话，我们需要打电话的时候就直接去引用打电话的功能就行了
#class Phone:
#    band = "苹果"
#    price = 8888
aaa = 111

#====== 知道类的定义，成员变量的定义 成员方法的定义，以及怎么实例化这个类，怎么去获取成员变量、成员方法

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