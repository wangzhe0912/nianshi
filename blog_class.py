#-*- coding: UTF-8 -*-
'''
Created on 2017.2.5

@author: Wangzhe
'''
import web
import model
from urlparse import unquote
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename
render = web.template.render('templates', base='base')
render_no_base = web.template.render('templates')
session = web.config._session

#博客页
class Blog(object):
    
    def get_blogs_for_four_parts(self):
        result_programming = list(model.get_basic_posts())[:6]
        result_deeplearning = list(model.get_dl_posts())[:6]
        result_testing = list(model.get_test_posts())[:6]
        result_perfect = list(model.get_perfect_posts())[:6]
        return [result_programming, result_deeplearning, result_testing, result_perfect]
           
    def GET(self):
        blogs = self.get_blogs_for_four_parts()
        return render.blog(blogs=blogs, session=session)

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
        if session.privilege != 2:
            return render_no_base.not_found404()
        blog_class = model.get_blog_class()
        return render.editor(list(blog_class))

    def POST(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = web.data()
        result = self.url_decode(data)
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
        if session.privilege != 2:
            return render_no_base.not_found404()
        blog_class = model.get_blog_class()
        return render.upload_blog(list(blog_class))
    
    def POST(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = web.input()
        blog_class = data.blog_class
        input_file = data.inputfile
        print input_file
        blog_content = self.trans_txt_to_html(input_file)
        title = data.title
        model.new_post(title, blog_content, blog_class)
        blog_class = model.get_blog_class()
        return web.seeother('/blog')


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
    def GET(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        model.del_post(int(id))
        raise web.seeother('/index')


class Edit:
    def GET(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)

    def POST(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/index')

class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts, session=session)
    
    def POST(self):
        posts = model.get_posts()
        return render.index(posts, session=session)


class IndexBasic(object):
    def GET(self):
        posts = list(model.get_basic_posts())
        return render.index(posts, session=session)


class IndexDl(object):
    def GET(self):
        posts = list(model.get_dl_posts())
        return render.index(posts, session=session)
    
    
class IndexTest(object):
    def GET(self):
        posts = list(model.get_test_posts())
        return render.index(posts, session=session)
    
    
class IndexPerfect(object):
    def GET(self):
        posts = list(model.get_perfect_posts())
        return render.index(posts, session=session)


class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post, session=session)
