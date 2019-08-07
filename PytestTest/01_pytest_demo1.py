# 导入pytest
import pytest

# 使用方法来管理测试用例
# 方法必须是 test_ 开头
# 第一个方法就称为一个测试用例
# 运行命令： pytest xxx.py
def test_add():
    assert 1+1 == 2

def test_istrue():
    assert False

def test_error():
    1/0
