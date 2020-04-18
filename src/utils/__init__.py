# -*- coding: utf-8 -*-
import random, string, json

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
def get_rotate_mode_value(mode):
    if mode == 'timing':
        return 1
    elif mode == 'flex':
        return 2
    elif mode == 'appoint':
        return 3
    return 0
