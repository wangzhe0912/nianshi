# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:48:32 2017

@author: 念师
"""

import web

import sys
import os
import time
import model
from webpyueditor import Ue_ImageUp, Ue_FileUp, Ue_ScrawlUp, Ue_GetRemoteImage, Ue_GetMovie, Ue_ImageManager



os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

web.config.debug = False

#整个网站的url映射
urls = ('/login', 'Login',
        '/log_out', 'LogOut',
        '/', 'Hello',
        '/contact', 'Contact',
        '/contact_index', 'IndexContact',
        '/view_contact/(\d+)', 'ViewContact',
        '/delete_contact/(\d+)', 'DeleteContact',
        
        '/blog', 'Blog',
        '/editor', 'Editor',
        '/upload_blog', 'UploadBlog',
        '/delete/(\d+)', 'Delete',
        '/edit/(\d+)', 'Edit',
        '/index', 'Index',
        '/index/(\d+)', 'Index',
        '/view/(\d+)', 'View',
        '/index_basic', 'IndexBasic',
        '/index_basic/(\d+)', 'IndexBasic',
        '/index_dl', 'IndexDl',
        '/index_dl/(\d+)', 'IndexDl',
        '/index_test', 'IndexTest',
        '/index_test/(\d+)', 'IndexTest',
        '/index_perfect', 'IndexPerfect',
        '/index_perfect/(\d+)', 'IndexPerfect',
        '/search', 'Search',
        '/new_blog_sets', 'NewBlogSet',
        '/view_blog_set/(\d+)', 'ViewBlogSet',
        '/view_blog_set/(\d+)/(\d+)', 'ViewBlogSet',
        '/owner/(\d+)', 'Owner',
        '/owner/(\d+)/(\d+)', 'Owner',
        '/video', 'Video',
        '/new_video', 'NewVideo',
        '/delete_video/(\d+)', 'DeleteVideo',
        '/edit_video/(\d+)', 'EditVideo',
        '/index_video', 'IndexVideo',
        '/view_video/(\d+)', 'ViewVideo',
        '/index_video_python', 'IndexVideoPython',
        '/index_video_db', 'IndexVideoDB',
        '/index_video_test', 'IndexVideoTest',
        '/index_video_fe', 'IndexVideoFE',
        '/index_video_dl', 'IndexVideoDL',
        '/search_video', 'SearchVideo',
        '/owner_video/(\d+)', 'OwnerVideo',
        
        '/tool', 'Tool',
        '/new_tool', 'NewTool',
        '/delete_tool/(\d+)', 'DeleteTool',
        '/edit_tool/(\d+)', 'EditTool',
        '/index_tool', 'IndexTool',
        '/view_tool/(\d+)', 'ViewTool',
        '/index_tool_software', 'IndexToolSoftware',
        '/index_tool_dl', 'IndexToolDL',
        '/index_tool_book', 'IndexToolBook',
        '/index_tool_ai', 'IndexToolAI',
        '/search_tool', 'SearchTool',
        '/owner_tool/(\d+)', 'OwnerTool',
        
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

from website_class import Login, LogOut, Hello, Contact, IndexContact, ViewContact, DeleteContact
from blog_class import Blog, Editor, UploadBlog, Delete, Edit, Index, IndexBasic, IndexDl
from blog_class import IndexPerfect, IndexTest, View, Search, NewBlogSet, ViewBlogSet, Owner
from video_class import Video, NewVideo, IndexVideo, DeleteVideo, EditVideo, IndexVideoDB, OwnerVideo
from video_class import IndexVideoDL, IndexVideoFE, IndexVideoPython,IndexVideoTest, ViewVideo, SearchVideo
from tool_class import Tool, NewTool, IndexTool, IndexToolAI, IndexToolBook, IndexToolDL
from tool_class import IndexToolSoftware, DeleteTool, EditTool, ViewTool, SearchTool, OwnerTool
# from tool_class import 

#配置template
render = web.template.render('templates', base='base')
render_no_base = web.template.render('templates')

config = web.storage(
    site_name='博客',
    datestr=model.transform_datestr
)


if __name__ == '__main__':
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()

