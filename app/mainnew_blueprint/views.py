# -*- coding: UTF-8 -*-
from flask import Flask
from . import mainnew#导入mainnew蓝本

@mainnew.route('/')#mainnew蓝本内路由
def index():


    return 'hello wor88888</h>'

