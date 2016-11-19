# -*- coding: UTF-8 -*-
from flask import Flask#程序包的构造文件
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap=Bootstrap()#实例化
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_new(config_name):
    appnew=Flask(__name__)
    appnew.config.from_object(config[config_name])
    config[config_name].init_app(appnew)
    # appnew.config.from_object(config[config_name])

    # config[config_name].init_app(appnew)

    bootstrap.init_app(appnew)#初始化
    mail.init_app(appnew)
    moment.init_app(appnew)
    db.init_app(appnew)


    from .mainnew_blueprint import mainnew
    appnew.register_blueprint(mainnew)#蓝本注册



    return appnew
