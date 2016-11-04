# -*- coding: UTF-8 -*-
from flask import Blueprint

mainnew = Blueprint('main',__name__)#创建蓝本实例

from . import views,errors #导入路由


