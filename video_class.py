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


#视频页
class Video(object):
    def get_videos_for_five_parts(self):
        result_python = list(model.get_video_python())[:6]
        result_sql = list(model.get_video_sql())[:6]
        result_test = list(model.get_video_test())[:6]
        result_dl = list(model.get_video_dl())[:6]
        result_fe = list(model.get_video_fe())[:6]
        return [result_python, result_sql, result_dl, result_test, result_fe]

    def GET(self):
        videos = self.get_videos_for_five_parts()
        print videos
        return render.video(videos=videos, session=session)


class NewVideo(object):
    def GET(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        video_class = model.get_video_class()
        return render.new_video(list(video_class), session=session)
    
    def POST(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = web.input()
        title = data.title
        video_class = data.video_class
        describe = data.describe
        url = data.url
        password = data.password
        model.new_video(title, describe, video_class, url, password)
        return web.seeother('/video')


class DeleteVideo(object):
    pass


class EditVideo(object):
    pass


class IndexVideo(object):
    pass


class ViewVideo(object):
    pass


class IndexVideoPython(object):
    pass


class IndexVideoDB(object):
    pass


class IndexVideoTest(object):
    pass



class IndexVideoFE(object):
    pass


class IndexVideoDL(object):
    pass