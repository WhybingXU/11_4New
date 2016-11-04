# -*- coding: UTF-8 -*-
#启动脚本
from flask_script import Manager
from app import creat_new

app = creat_new( 'default')
manage=Manager(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    manage.run()
