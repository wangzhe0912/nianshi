# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:46:48 2017

@author: 念师
"""

import web
import datetime

db = web.database(dbn='mysql', db='nianshi', user='root', pw='Sdl!19940208', charset="utf8")

def transform_datestr(posted_on):
    datetime_obj = datetime.datetime.strptime(posted_on, '%Y-%m-%d %H:%M:%S.%f')
    return web.datestr(datetime_obj)

def check_pwd(username, password):
    records = db.select('login', where='username=$username', vars=locals())
    if len(records) == 0:
        result = {"status": False, "result": None, "desc": "username doesn't exist!"}
    else:
        record = records[0]
        if record.password == password:
            result = {"status": True, "result": record, "desc": "Log in successful!"}
        else:
            result = {"status": False, "result": None, "desc": "password is not correct!"}
    return result

def get_posts_by_keywords(keywords, from_class):
    from urllib import unquote
    number = len(keywords)
    where_sentence = ' where '
    for keyword in keywords:
        where_sentence += 'title like "%' + unquote(keyword) + '%" and '
    print 'select * from ' + from_class + where_sentence[:-4]
    result = db.query('select * from ' + from_class + where_sentence[:-4])
    # result = db.select(from_class, where='$where_sentence[:-4]', vars=locals())
    return result

def new_contact(theme, comments, contact_way, status):
    db.insert('contact', theme=theme, comments=comments, contact_way=contact_way,
            status=status, posted_on=datetime.datetime.now())

def del_contact(id):
    db.delete('contact', where='id=$id', vars=locals())

def get_contacts():
    return db.select('contact', order='id desc')

def get_contact(id):
    try:
        return db.select('contact', where='id=$id',
                         vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text, blog_class):
    db.insert('blog', title=title, content=text,
              blog_class = blog_class,
              posted_on=datetime.datetime.now())

def new_post_set(title, class_name):
    return db.insert('series', name=title, class_name=class_name)

def add_blog_series(series_id, id_list):
    db.update('blog', where='id in $id_list', vars=locals(), series_id=series_id)

def get_blog_set_posts(id):
    result = db.query('select b.title title, b.id id, b.blog_class blog_class, b.posted_on posted_on from blog b, series s where b.series_id=s.id order by b.title')
    return result

def del_post(id):
    db.delete('blog', where='id=$id', vars=locals())

def update_post(id, title, text):
    db.update('blog', where='id=$id', vars=locals(),
              title=title, content=text)

def get_posts():
    return db.select('blog', order='id desc')

def get_post(id):
    try:
        return db.select('blog', where='id=$id',
                         vars=locals())[0]
    except IndexError:
        return None

def get_basic_posts():
    return db.select('blog', where='blog_class=1', order='id desc')

def get_dl_posts():
    return db.select('blog', where='blog_class=2', order='id desc')

def get_test_posts():
    return db.select('blog', where='blog_class=3', order='id desc')

def get_perfect_posts():
    return db.select('series', order='id desc')

def get_blog_class():
    return db.select('blog_class')

# def get_blogs_programming():
#     return db.select('blog', where='blog_class=1', order='id desc')
# 
# def get_blogs_deeplearing():
#     return db.select('blog', where='blog_class=2', order='id desc')
# 
# def get_blogs_testing():
#     return db.select('blog', where='blog_class=3', order='id desc')
# 
# def get_blogs_perfect():
#     return db.select('blog', where='blog_class=4', order='id desc')

def new_video(title, describe, video_class, url, password):
    resource_id = db.insert('resource', url=url, password=password)
    db.insert('video', title=title, detail=describe,
              video_class = video_class, resource_id=resource_id,
              posted_on=datetime.datetime.now())

def del_video(id):
    db.delete('video', where='id=$id', vars=locals())

def update_video(id, title, describe, video_class, url, password):
    resource_id = db.insert('resource', url=url, password=password)
    db.update('video', where='id=$id', vars=locals(),
              title=title, detail=describe,
              video_class = video_class, resource_id=resource_id)

def get_video(id):
    return db.select('video', where='id=$id', vars=locals())[0]

def get_videos():
    return db.select('video', order='id desc')

def get_video_class():
    return db.select('video_class')

def get_video_python():
    return db.select('video', where='video_class=1', order='id desc')

def get_video_sql():
    return db.select('video', where='video_class=2', order='id desc')

def get_video_dl():
    return db.select('video', where='video_class=3', order='id desc')

def get_video_fe():
    return db.select('video', where='video_class=4', order='id desc')

def get_video_test():
    return db.select('video', where='video_class=5', order='id desc')


def new_tool(title, describe, tool_class, url, password):
    resource_id = db.insert('resource', url=url, password=password)
    db.insert('tool', title=title, detail=describe,
              tool_class = tool_class, resource_id=resource_id,
              posted_on=datetime.datetime.now())

def del_tool(id):
    db.delete('tool', where='id=$id', vars=locals())

def update_tool(id, title, describe, tool_class, url, password):
    resource_id = db.insert('resource', url=url, password=password)
    db.update('tool', where='id=$id', vars=locals(),
              title=title, detail=describe,
              tool_class = tool_class, resource_id=resource_id)

def get_tool(id):
    return db.select('tool', where='id=$id', vars=locals())[0]

def get_tools():
    return db.select('tool', order='id desc')

def get_tool_class():
    return db.select('tool_class')

def get_tool_software():
    return db.select('tool', where='tool_class=1', order='id desc')

def get_tool_book():
    return db.select('tool', where='tool_class=2', order='id desc')

def get_tool_ai():
    return db.select('tool', where='tool_class=3', order='id desc')

def get_tool_dl():
    return db.select('tool', where='tool_class=4', order='id desc')


def get_resource(id):
    return db.select('resource', where='id=$id', vars=locals())[0]


