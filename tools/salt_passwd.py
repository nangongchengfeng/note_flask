# -*- coding: utf-8 -*-
# @Time    : 2022/11/29 17:14
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : salt_passwd.py
# @Software: PyCharm
# -------------------------------------------
# Python简单密码加密程序
# 随机生成4位salt，与原始密码组合，通过md5加密
# Author : Lrg
# -------------------------------------------
# encoding = utf-8
import hmac
from random import Random
from hashlib import md5


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update(pwd + salt)
    return md5_obj.hexdigest()


def password_new(salt, password, dig='sha1'):
    """
    :param salt: 盐
    :param password: 加密的字符
    :return:
    """

    h1 = hmac.new( password.encode(), digestmod=dig)

    return h1.hexdigest()


if __name__ == '__main__':
    print(password_new('123456', 'yan1gbeita'))
