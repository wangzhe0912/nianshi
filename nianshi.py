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
        '/blog', 'Blog',
        '/index', 'Index',
        '/save', 'Save',
        '/', 'Hello',)


class Hello(object):
    def GET(self):
        return "Hello World!"

        
class Blog(object):
    def GET(self):
        return render.blog(u'念师')


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

