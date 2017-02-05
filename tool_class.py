#-*- coding: UTF-8 -*-
'''
Created on 2017.2.5

@author: Wangzhe
'''
import web
import model
render = web.template.render('templates', base='base')
render_no_base = web.template.render('templates')
session = web.config._session
