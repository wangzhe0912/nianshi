# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:48:32 2017

@author: 念师
"""

import web
from urlparse import unquote
import sys
import os
import time
import model
from webpyueditor import Ue_ImageUp, Ue_FileUp, Ue_ScrawlUp, Ue_GetRemoteImage, Ue_GetMovie, Ue_ImageManager
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename

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
        '/', 'Hello',
        #editor
        '/view/(\d+)', 'View',
#         '/new', 'New',
        '/upload_blog', 'UploadBlog',
        '/delete/(\d+)', 'Delete',
        '/edit/(\d+)', 'Edit',
        '/imgs/(.*)', 'Imgs',
        '/ue_imageUp', Ue_ImageUp,
        '/ue_fileUp', Ue_FileUp,
        '/ue_scrawlUp', Ue_ScrawlUp,
        '/ue_getRemoteImage', Ue_GetRemoteImage,
        '/ue_getMovie', Ue_GetMovie,
        '/ue_imageManager', Ue_ImageManager,)

#APP服务
app = web.application(urls, globals())

#初始化了一个session
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer = {'login_status': 0, 'username':'','privilege': 0})
web.config._session = session

#配置template
render = web.template.render('templates', base='base')
config = web.storage(
    site_name='博客',
    datestr=model.transform_datestr
)



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
    
    def get_blogs_for_four_parts(self):
        result_programming = list(model.get_blogs_programming())[:6]
        result_deeplearning = list(model.get_blogs_deeplearing())[:6]
        result_testing = list(model.get_blogs_testing())[:6]
        result_perfect = list(model.get_blogs_perfect())[:6]
        return [result_programming, result_deeplearning, result_testing, result_perfect]
           
    def GET(self):
        blogs = self.get_blogs_for_four_parts()
        return render.blog(blogs=blogs)

#博客编辑页
class Editor(object):
    
    def url_decode(self, encode_str):
        result_list = encode_str.split('&')
        result_dict = {}
        for key, value in [x.split('=') for x in result_list]:
            if key == "content":
                print value
                value = value.replace('+', ' ')
                print value
            result_dict[key] = unquote(value)
        return result_dict
    
    def GET(self):
        blog_class = model.get_blog_class()
        return render.editor(list(blog_class))

#     def POST(self):
#         data = web.data().split('=')[-1]
#         result = unquote(data)
#         print result
#         web.seeother('/editor')
    def POST(self):
        data = web.data()
        print data
        print "*********"
        result = self.url_decode(data)
        print result
        model.new_post(result['title'], result['content'], result['blog_class'])
        raise web.seeother('/blog')


class UploadBlog(object):
    
    def get_html_text(self, plain_text, language_suffix):
        #formatter = HtmlFormatter(encoding='utf-8', style = 'emacs', linenos = True)
        formatter = HtmlFormatter(encoding='utf-8', style = 'emacs', linenos = True)
        lexer = get_lexer_for_filename('a.' + language_suffix.lower())
        return highlight(plain_text, lexer, formatter)
    
    def trans_txt_to_html(self, txt):
        result = "<p>"
        space_line = 0
        script = ""
        script_tag = 0
        language_suffix = ''
        for line in txt:
            if "***script***" in line:
                #开始标本语言
                language_suffix = line.split()[-1]
                script_tag = 1
                continue
            elif "***script_end***" in line:
                #脚本语言结束
                script_tag = 0
                result += self.get_html_text(script, language_suffix)
                script = ""
                language_suffix = ""
                continue
            elif script_tag == 1:
                #如果属于脚本内容
                script += line
                continue
            #此后都与脚本无关
            if not line.strip():
                #如果是空行
                if space_line == 0:
                    #如果上一行不是空行
                    if result:
                        result += '</p>'
                    space_line = 1
                    continue
                else:
                    #如果上一行就是空行
                    result += '<br/>'
            else:
                #如果不是空行
                if space_line != 0:
                    result += '<p>'
                line.replace(" ", "&nbsp")
                result += line.strip()
                space_line = 0
        result += '<link rel="stylesheet" href="../static/css/highlight.css">'
        return result
    
    def GET(self):
        blog_class = model.get_blog_class()
        return render.upload_blog(list(blog_class))
    
    def POST(self):
        data = web.input()
        blog_class = data.blog_class
        input_file = data.inputfile
        print input_file
        blog_content = self.trans_txt_to_html(input_file)
        title = data.title
        model.new_post(title, blog_content, blog_class)
        blog_class = model.get_blog_class()
        return web.seeother('/blog')

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


#编辑器部分
class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)


class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)


class New:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
                         size=30,
                         description=u'日志标题'),
        web.form.Textarea('content', web.form.notnull,
                          rows=30, cols=80,
                          description=u'日志内容'),
        web.form.Button(u'提交')
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')


class Delete:
    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:
    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)

    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')


class Imgs:
    def GET(self, name):
        ext = name.split(".")[-1]
        cType = {
            "png": "images/png",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"
        }
        if name in os.listdir('imgs'):
            web.header("Content-Type", cType[ext])
            return open('imgs/%s' % name, "rb").read()
        else:
            raise web.notfound()


if __name__ == '__main__':
    app.run()

