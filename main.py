# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:50
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : main.py
# @Software: PyCharm
# 它是 Flask 程序的入口
from app import app
from flask import render_template, session

import db
from application.users import users
from application.todos import todos

app.register_blueprint(users.blueprint)
app.register_blueprint(todos.blueprint)
from tools.logs import log
from tools.iptool import get_request_ip



@app.route("/")
def index():
    log.logger.info(f"{get_request_ip()}点击开始页面")
    hasLogin = session.get("hasLogin")
    if hasLogin:
        userId = session.get('userId')
        items = db.getTodos(userId)
        todos = [item for item in items if item.status == 'todo']
        dones = [item for item in items if item.status == 'done']
        log.logger.info(f"{get_request_ip()} 登录成功，用户ID：{userId}")
    else:
        todos = []
        dones = []
        log.logger.info(f"{get_request_ip()} 没有登录")
    return render_template('index.html', hasLogin=hasLogin, todos=todos, dones=dones)


app.run(debug=True, port=5000)
