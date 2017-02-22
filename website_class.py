#-*- coding: UTF-8 -*-
'''
Created on 2017.2.5

@author: Wangzhe
'''

import web
import model
import smtplib
from email.mime.text import MIMEText

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
            session.userId = result['result']['id']
            session.login_status = 1
            if not result['result']['admin'] and result['result']['general_user']:
                #师子的privilege编号是1
                session.privilege = 1
            elif result['result']['admin'] and not result['result']['general_user']:
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

#联系我们页
class Contact(object):
    def GET(self):
        return render.contact(session=session)

    def POST(self):
        data = web.input()
        print data
        HOST = 'smtp.tju.edu.cn'
        SUBJECT = data.theme
        TO = "1658563602@qq.com"
        FROM = "wangzhe0912@tju.edu.cn"
        msg = MIMEText('<table width="800" border="0" cellspacing="0" cellpadding="4">\
              <tr><td bgcolor="#CECFAD" height="20" style="font-size:14px"></td></tr>\
              <tr><td bgcolor="#EFEBDE" height="100" style="font-size:13px">详细信息：'\
              + data.comments + '</td></tr>' +\
              '<tr><td bgcolor="#EFEBDE" height="100" style="font-size:13px">联系方式：'\
              + data.contact_way + '</td></tr></table>',"html","utf-8")
        msg['Subject'] = SUBJECT
        msg['From']=FROM
        msg['To']=TO
        try:
            server = smtplib.SMTP()
            server.connect(HOST,"25")
            server.starttls()
            server.login("wangzhe0912@tju.edu.cn","qxq102132")
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
            model.new_contact(data.theme, data.comments, data.contact_way, 'Success')
        except Exception, e: 
            model.new_contact(data.theme, data.comments, data.contact_way, 'Fail')
            print "失败："+str(e)
        web.seeother('/') 


class IndexContact(object):
    def GET(self):
        contacts = model.get_contacts()
        return render.index_contact(contacts, session=session)


class ViewContact(object):
    def GET(self, id):
        contact = model.get_contact(id)
        return render.contact_info(contact, session=session)


class DeleteContact(object):
    def GET(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        model.del_contact(int(id))
        raise web.seeother('/contact_index')