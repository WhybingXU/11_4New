# -*- coding: UTF-8 -*-
from flask import render_template
from datetime import datetime
from . import mainnew#导入mainnew蓝本

@mainnew.route('/<name>')#mainnew蓝本内路由
def index(name):


    return render_template('index.html',name=name)

