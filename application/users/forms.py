# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 12:04
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField(
        label='姓名',
        validators=[
            DataRequired(message='姓名不能为空')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )

    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    name = StringField(
        label='姓名',
        validators=[
            DataRequired(message='姓名不能为空')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )

    submit = SubmitField('注册')
