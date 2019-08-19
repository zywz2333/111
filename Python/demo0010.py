import re

"""
a = "吴俊彬吴大彬吴小彬"
b = re.match("^吴(.*?)彬$", a).group()
# b = re.match("吴(.*?)彬", a).group()
print(b)
c = re.search("吴(.*?)彬", a).group()
print(c)
d = re.findall("吴(.*?)彬", a)
print(d)
"""
def match():
    """
        match：只能够匹配开头
    """
    a = "老铁啊我太难了啊"
    b = re.match("啊", a).group()
    print(b)

if __name__ == "__main__":
    match()    
