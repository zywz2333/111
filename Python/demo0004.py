'''
pymysql是一个用来操作mysql数据库的包
'''
import pymysql

dbinfo = {
    "host":"118.24.29.59",
    "user":"vn",
    "password":"1qaz!QAZ123",
    "db":"lux"
}

# pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test_langjin")
def qurey(sql):
    '''
    这个方法是查询数据库用的
    '''
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL语句
        res = cursor.fetchall()  # 获取所有的返回值
        db.close()  # 关闭数据库连接
        return res
    except:
        return None


def commit(sql):
    '''
    这个方法是修改数据库用的,新增、修改、删除
    '''
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL语句
        db.commit()  # 应用
        db.close()  # 关闭数据库连接
        return True
    except:
        return False







