# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:41
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : app.py
# @Software: PyCharm


@app.route('/')
def index():
    return "<h1>Hello, flask!</h1>"


@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name


@app.route('/calc/')
def calc():
    start = "1988"
    today = "2018"
    rel = int(today) - int(start)
    return "<h1>This year is Pingan's %sth anniversary, congratulations!</h1>" % rel


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
    # app.run()
