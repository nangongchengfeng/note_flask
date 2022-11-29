# -*- coding: utf-8 -*-
# @Time    : 2022/11/9 14:23
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : iptools.py
# @Software: PyCharm
# import logging

from flask import request


def get_request_ip():
    """
    查询本机ip地址
    :return: ip
    """

    '''获取请求方的ip'''
    try:
        ip = request.remote_addr
        # logging.error('------ ip = %s ------' % ip)
        return ip
    except Exception as e:
        print(e)

    # return ip


if __name__ == '__main__':
    print(get_request_ip())
