# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:46:48 2017

@author: 念师
"""

import web
import datetime

db = web.database(dbn='mysql', db='nianshi', user='root', pw='123', charset='utf8')

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
    return db.select('entries', order='id desc')


def get_post(id):
    try:
        return db.select('entries', where='id=$id',
                         vars=locals())[0]
    except IndexError:
        return None


def new_post(title, text):
    db.insert('entries', title=title, content=text,
              posted_on=datetime.datetime.utcnow())


def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())


def update_post(id, title, text):
    db.update('entries', where='id=$id', vars=locals(),
              title=title, content=text)


def transform_datestr(posted_on):
    datetime_obj = datetime.datetime.strptime(posted_on, '%Y-%m-%d %H:%M:%S.%f')
    return web.datestr(datetime_obj)