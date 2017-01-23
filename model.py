# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:46:48 2017

@author: 念师
"""

import web

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