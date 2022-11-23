# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:41
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : app.py
# @Software: PyCharm
from flask import Flask
from datetime import timedelta

app = Flask(__name__)
#配置缓存的有效时间；
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
#在程序中使用到了 Session，需要使用 SECRET_KEY 进行加密
app.config['SECRET_KEY'] = 'P5Yv#alBh6*dq#96'



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
    # app.run()
