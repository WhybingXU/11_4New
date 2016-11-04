# -*- coding: UTF-8 -*-
from flask import render_template
from . import mainnew

@mainnew.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'),404

@mainnew.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
