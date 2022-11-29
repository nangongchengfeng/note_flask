# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:51
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : users.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, session
from flask import Blueprint
import db
from application.users.forms import LoginForm, RegisterForm

blueprint = Blueprint('users', __name__, url_prefix='/users')




@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm()
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            user = db.login(name, password)
            if user:
                session['hasLogin'] = True
                session['userId'] = user.userId
                return redirect('/')
        return render_template('login.html', form=form)



@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)
    else:
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            if db.register(name, password):
                return redirect('/')
        return render_template('register.html', form=form)


@blueprint.route('/logout')
def logout():
    session['hasLogin'] = False
    return redirect('/')
