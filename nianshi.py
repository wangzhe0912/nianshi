# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:48:32 2017

@author: 念师
"""

import web
from urlparse import unquote
import sys
import os
import model

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

web.config.debug = False


urls = (
        '/index', 'Index',
        '/save', 'Save',
        '/login', 'Login',
        '/about', 'About',
        '/contact', 'Contact',
        '/blog', 'Blog',
        '/tools', 'Tools',
        '/video', 'Video',
        '/logout', 'Logout',
        '/log_out', 'LogOut',
        '/', 'Hello',)

app = web.application(urls, globals())

#初始化了一个session
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer = {'login_status': 0, 'username':'','privilege': 0})
web.config._session = session


render = web.template.render('templates', base='base')

class Login(object):
    def check_pwd(self, username, password):
        result = model.check_pwd(username, password)
        return result
        

    def GET(self):
        if session.login_status:
            return render.homepage(True,session.username)
        else:
            return render.login()

    def POST(self):
        data = web.input()
        username = data['form-username']
        password = data['form-password']
        result = self.check_pwd(username, password)
        if not result["status"]:
            return render.login(result=False, desc=result["desc"])
        else:
            session.username = result['result']['username']
            session.login_status = 1
            if not result['result']['admin'] and result['result']['shizi']:
                session.privilege = 1
            elif result['result']['admin'] and not result['result']['shizi']:
                session.privilege = 2   
            else:
                session.privilege = 0
            return render.homepage(True, result['result']['username'])
        

class LogOut(object):
    def GET(self):
        session.username =''
        session.login_status = 0
        session.privilege = 0
        return render.login()
     

class About(object):
    def GET(self):
        return u"关于"


class Contact(object):
    def GET(self):
        return u"联系我们"


class Blog(object):
    def GET(self):
        return render.blog()


class Tools(object):
    def GET(self):
        return u"工具"


class Video(object):
    def GET(self):
        return u"视频"


class Hello(object):
    def GET(self):
        if session.login_status==1:
            return render.homepage(True, session.username)
        else:
            return render.homepage(False, '')


class Index(object):
    def GET(self):
        return render.index()
    def POST(self, content):
        print "********************"
        print content
        print "********************"


class Save(object):
    def POST(self):
        print "*******12321***********"
        data = web.data().split('=')[-1]
        print unquote(data)
        print "****231****"
       

        
if __name__ == '__main__':
    app.run()

