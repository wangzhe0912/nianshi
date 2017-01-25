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

web.config.debug = True

#整个网站的url映射
urls = ('/login', 'Login',
        '/about', 'About',
        '/contact', 'Contact',
        '/blog', 'Blog',
        '/tools', 'Tools',
        '/video', 'Video',
        '/log_out', 'LogOut',
        '/editor', 'Editor',
        '/', 'Hello',)

#APP服务
app = web.application(urls, globals())

#初始化了一个session
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer = {'login_status': 0, 'username':'','privilege': 0})
web.config._session = session

#配置template
render = web.template.render('templates', base='base')

#访问主页
class Hello(object):
    def GET(self):
        try:
            if session.login_status==1:
                return render.homepage(True, session.username)
            else:
                return render.homepage(False, '')
        except:
            return render.homepage(False, '')
        
#访问登录页
class Login(object):
    def check_pwd(self, username, password):
        result = model.check_pwd(username, password)
        return result

    def GET(self):
        try:
            if session.login_status:
                return  web.seeother('/')
            else:
                return render.login()
        except:
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
                #师子的privilege编号是1
                session.privilege = 1
            elif result['result']['admin'] and not result['result']['shizi']:
                #admin的privilege编号是2
                session.privilege = 2   
            else:
                session.privilege = 0
            return web.seeother('/')

#退出
class LogOut(object):
    def GET(self):
        session.username =''
        session.login_status = 0
        session.privilege = 0
        return render.login()
     
#博客页
class Blog(object):
    def GET(self):
        return render.blog()

#博客编辑页
class Editor(object):
    def GET(self):
        return render.editor()

    def POST(self):
        data = web.data().split('=')[-1]
        result = unquote(data)
        web.seeother('/editor')

#工具页
class Tools(object):
    def GET(self):
        return u"工具"

#视频页
class Video(object):
    def GET(self):
        return u"视频"
       
#关于页
class About(object):
    def GET(self):
        return u"关于"

#联系我们页
class Contact(object):
    def GET(self):
        return u"联系我们"


if __name__ == '__main__':
    app.run()

