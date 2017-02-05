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

#访问主页
class Hello(object):
    def GET(self):
        return render.homepage(session=session)
    
        
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
        web.seeother('/')
        
#关于页
class About(object):
    def GET(self):
        return u"关于"

#联系我们页
class Contact(object):
    def GET(self):
        return u"联系我们"