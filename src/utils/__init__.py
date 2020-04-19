# -*- coding: utf-8 -*-
import random, string, json
from enum import Enum

def response_json(data={}, msg='ok', code=0):
    return {
        'code': code,
        'msg': msg,
        'data': data
    }

# 生成长度为 length 位的随机字符串
def generate_random_str(length):
    """
    Args:
        length: An int value indicate the length of random string

    Returns:
        A random string
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# 轮换模式
class RotateMode(Enum):
    HARD = 0,
    SOFT = 1,
    MANNUAL = 2
