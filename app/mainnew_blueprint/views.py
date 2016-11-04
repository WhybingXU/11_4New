# -*- coding: UTF-8 -*-
from flask import render_template,session,flash,redirect,url_for
from .form import NameForm
from datetime import datetime
from . import mainnew#导入mainnew蓝本

@mainnew.route('/', methods=['GET', 'POST'])#mainnew蓝本内路由
def index(name):
    form=NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name!=form.name.data:
            flash('changed name')
        session['name']=form.name.data
        return redirect(url_for('index'))#重定向
    return render_template('index.html',form=form,name=session.get('name'))

