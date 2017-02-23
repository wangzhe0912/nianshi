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
        if session.privilege == 0:
            return render_no_base.not_found404()
        video_class = model.get_video_class()
        return render.new_video(list(video_class), session=session)
    
    def POST(self):
        if session.privilege == 0:
            return render_no_base.not_found404()
        data = web.input()
        title = data.title
        video_class = data.video_class
        describe = data.describe
        url = data.url
        password = data.password
        model.new_video(title, describe, video_class, url, password, session.userId)
        return web.seeother('/video')


class DeleteVideo(object):
    def GET(self, id):
        owner = model.get_video_owner(id).owner
        if session.privilege != 2 and session.userId != owner:
            return render_no_base.not_found404()
        model.del_video(int(id))
        raise web.seeother('/index_video')


class EditVideo(object):
    def GET(self, id):
        owner = model.get_video_owner(id).owner
        if session.privilege != 2 and session.userId != owner:
            return render_no_base.not_found404()
        data = model.get_video(int(id))
        resource_id = data.resource_id
        resource_data = model.get_resource(resource_id)
        video_classes = list(model.get_video_class())
        return render.edit_video(data, resource_data, video_classes, session, id)

    def POST(self, id):
        owner = model.get_video_owner(id).owner
        if session.privilege != 2 and session.userId != owner:
            return render_no_base.not_found404()
        data = web.input()
        model.update_video(int(id), data.title, data.describe,
                          data.video_class, data.url, data.password)
        raise web.seeother('/index_video')


class IndexVideo(object):
    def GET(self):
        videos = model.get_videos()
        return render.index_video(videos, session=session)


class ViewVideo(object):
    def GET(self, id):
        video = model.get_video(int(id))
        resource_id = video.resource_id
        resource = model.get_resource(resource_id)
        return render.view_video(video, resource, session=session)


class IndexVideoPython(object):
    def GET(self):
        videos = list(model.get_video_python())
        return render.index_video(videos, session=session)


class IndexVideoDB(object):
    def GET(self):
        videos = list(model.get_video_sql())
        return render.index_video(videos, session=session)


class IndexVideoTest(object):
    def GET(self):
        videos = list(model.get_video_test())
        return render.index_video(videos, session=session)


class IndexVideoFE(object):
    def GET(self):
        videos = list(model.get_video_fe())
        return render.index_video(videos, session=session)


class IndexVideoDL(object):
    def GET(self):
        videos = list(model.get_video_dl())
        return render.index_video(videos, session=session)


class SearchVideo(object):
    def POST(self):
        key_words = web.data().split('=')[1].split('+')
        print key_words
        # ["srch-term"].split()
        videos = list(model.get_posts_by_keywords(key_words, 'video'))
        return render.index_video(videos, session=session)


class OwnerVideo(object):
    def GET(self, id):
        videos = list(model.get_videos_for_person(id))
        return render.index_video(videos, session=session)