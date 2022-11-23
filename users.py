# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:51
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : users.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask import Blueprint
import db

blueprint = Blueprint('users', __name__, url_prefix='/users')