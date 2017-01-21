# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:48:32 2017

@author: 念师
"""

import web
from urlparse import unquote
import sys
import os

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
        '/', 'Hello',)

class Login(object):
    def GET(self):
        return u"请登录"


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
        return render.homepage()


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

