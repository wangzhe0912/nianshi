# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:46:48 2017

@author: 念师
"""

import web
import datetime

db = web.database(dbn='mysql', db='nianshi', user='root', pw='123', charset="utf8")

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

def get_posts():
    return db.select('blog', order='id desc')


def get_post(id):
    try:
        return db.select('blog', where='id=$id',
                         vars=locals())[0]
    except IndexError:
        return None


def new_post(title, text, blog_class):
    db.insert('blog', title=title, content=text,
              blog_class = blog_class,
              posted_on=datetime.datetime.now())


def del_post(id):
    db.delete('blog', where='id=$id', vars=locals())


def update_post(id, title, text):
    db.update('blog', where='id=$id', vars=locals(),
              title=title, content=text)


def transform_datestr(posted_on):
    datetime_obj = datetime.datetime.strptime(posted_on, '%Y-%m-%d %H:%M:%S.%f')
    return web.datestr(datetime_obj)

def get_blog_class():
    return db.select('blog_class')

def get_blogs_programming():
    return db.select('blog', where='blog_class=1', order='id desc')

def get_blogs_deeplearing():
    return db.select('blog', where='blog_class=2', order='id desc')

def get_blogs_testing():
    return db.select('blog', where='blog_class=3', order='id desc')

def get_blogs_perfect():
    return db.select('blog', where='blog_class=4', order='id desc')



