# -*- coding: UTF-8 -*-
# from flask import render_template,session,flash,redirect,url_for
# from .form import NameForm
# from datetime import datetime
# from . import mainnew  #导入mainnew蓝本
#
#
#
#
# @mainnew.route('/', methods=['GET', 'POST'])#mainnew蓝本内路由
# def index(name):
#     form=NameForm()
#     if form.validate_on_submit():
#         old_name=session.get('name')
#         if old_name is not None and old_name!=form.name.data:
#             flash('changed name')
#         session['name']=form.name.data
#         return redirect(url_for('.index'))#重定向
#     return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False),current_time=datetime.utcnow())


from flask import render_template, session, redirect, url_for, current_app
from . import mainnew
from .form import NameForm


@mainnew.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))