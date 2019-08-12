print(1234)
print("1234")






hint = 1234  # 整数
hstr = "字符串111111111111111111111111111111111111111111111"  # 字符串
hfolat = 2.333  #  小数
hbool = True   # 布尔值



hnone = None   # 空



bltype = type(hnone)
print(bltype)


print("111"+"222")



htuple = (1,"字符串",2.333,"abc","远航",1,"字符串",2.333,"abc","远航",1,"字符串",2.333,"abc","远航")   # 元组


num = htuple.count("abc")  #  统计这个叫htuple的元组里面有多少个叫abc的值
print(num)

xxx = htuple.index("abc")  # 找出htuple里面最近的叫abc的值的下标
print(xxx)


hlist = [1,2,3,"哈哈","喜喜","随便"]   # 数组/列表  二维数组
del hlist[0]
hlist.append("哈哈")   # append的作用，往数组里新增值
hlist2 = hlist.copy()  # copy就是复制原来的数组，赋值给另一个值
num = hlist.count("abc") # 统计
hlist.extend("haha")  # extend把字符串拆分为单个值，添加到数组中
num = hlist.index("哈哈")  # 计算下标
hlist.insert(0,"第一位")  # 控制数据深入数组的位置
value = hlist.pop(0)  # 移走某个值
hlist.remove("哈哈")  # 删除某个值
print(hlist)
hlist.clear()  # clear清空数组里的所有值


print("--------------分割线---------------------")
 # 字典 键值对  key:value
hdict = {
    "name":"张三",
    "high":"173cm",
    "key":"value",
    "dict1":{
        "name2":"李四"
    }}  

value = hdict.get("name1")  # get就是通过key取值
print(value)

value = hdict.pop("name") # 取走
print(value)
print(hdict)




# 补充：20190812 isinstance
aaa = "sss"
bbb = 10
ccc = 10.0
ddd = True
fff = [1,2,3,4]
ggg = (1,2,3,5)
hhh = {"username":"小坤坤", "question":"isinstance"}
jjj = None

print("============================")
print(type(aaa)) # str
print(type(bbb)) # int 
print(type(ccc)) # float
print(type(ddd)) # bool
print(type(fff)) # list
print(type(ggg)) # tuple
print(type(hhh)) # dict
print(type(jjj)) # NoneType

print(isinstance(aaa, list))
print(isinstance(ggg, tuple))
