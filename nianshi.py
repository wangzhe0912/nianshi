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

render = web.template.render('templates', base='base')

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

class Login(object):
    def check_pwd(self, username, password):
        result = model.check_pwd(username, password)
        return result
        

    def GET(self):
        return render.login()

    def POST(self):
        data = web.input()
        username = data['form-username']
        password = data['form-password']
        result = self.check_pwd(username, password)
        if not result["status"]:
            return render.homepage(False, result["desc"])
        else:
            web.setcookie('name', result['result']['username'], 3600)
            web.setcookie('admin', result['result']['admin'], 3600)
            web.setcookie('shizi', result['result']['shizi'], 3600)
            return render.homepage(True, result['result']['username'])
        

class Logout(object):
    def GET(self):
        web.cookies().clear()
        print web.cookies()
        #web.redirect('/')
        return 1+1


class LogOut(object):
    def GET(self):
        web.cookies()
        print web.cookies()
        #web.redirect('/')
        return 1+1
        

class About(object):
    def GET(self):
        return u"关于"


class Contact(object):
    def GET(self):
        return u"联系我们"


class Blog(object):
    def GET(self):
        return u"博客"


class Tools(object):
    def GET(self):
        return u"工具"


class Video(object):
    def GET(self):
        return u"视频"


class Hello(object):
    def GET(self):
        if 'name' in web.cookies():
            return render.homepage(True, web.cookies().name)
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
    app = web.application(urls, globals())
    app.run()

