import datetime

def get_now():
    """
        获取当前时间
    """
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
