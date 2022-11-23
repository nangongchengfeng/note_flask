# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 9:51
# @Author  : weidongliang
# @Email   : 1794748404@qq.com
# @File    : todos.py
# @Software: PyCharm

from flask import Flask, render_template, request, redirect, session, jsonify
from flask import Blueprint
import db

blueprint = Blueprint('todos', __name__, url_prefix='/todos')