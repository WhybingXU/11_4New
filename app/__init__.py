# -*- coding: UTF-8 -*-
from flask import Flask#程序包的构造文件
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from config import config

bootstrap=Bootstrap()#实例化
moment=Moment()

def creat_new():
    appnew=Flask(__name__)
    # appnew.config.from_object(config[config_name])

    # config[config_name].init_app(appnew)

    bootstrap.init_app(appnew)#初始化
    moment.init_app(appnew)


    from .mainnew_blueprint import mainnew
    appnew.register_blueprint(mainnew)#蓝本注册



    return appnew