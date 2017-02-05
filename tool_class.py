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
class Tool(object):
    def get_tools_for_four_parts(self):
        result_software = list(model.get_tool_software())[:6]
        result_book = list(model.get_tool_book())[:6]
        result_ai = list(model.get_tool_ai())[:6]
        result_dl = list(model.get_tool_dl())[:6]
        return [result_software, result_book, result_ai, result_dl,]

    def GET(self):
        tools = self.get_tools_for_four_parts()
        return render.tool(tools=tools, session=session)


class NewTool(object):
    def GET(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        tool_class = model.get_tool_class()
        return render.new_tool(list(tool_class), session=session)
    
    def POST(self):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = web.input()
        title = data.title
        tool_class = data.tool_class
        describe = data.describe
        url = data.url
        password = data.password
        model.new_tool(title, describe, tool_class, url, password)
        return web.seeother('/tool')


class DeleteTool(object):
    def GET(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        model.del_tool(int(id))
        raise web.seeother('/index_tool')


class EditTool(object):
    def GET(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = model.get_tool(int(id))
        resource_id = data.resource_id
        resource_data = model.get_resource(resource_id)
        tool_classes = list(model.get_tool_class())
        return render.edit_tool(data, resource_data, tool_classes, session, id)

    def POST(self, id):
        if session.privilege != 2:
            return render_no_base.not_found404()
        data = web.input()
        model.update_tool(int(id), data.title, data.describe,
                          data.tool_class, data.url, data.password)
        raise web.seeother('/index_tool')


class IndexTool(object):
    def GET(self):
        tools = model.get_tools()
        return render.index_tool(tools, session=session)


class ViewTool(object):
    def GET(self, id):
        tool = model.get_tool(int(id))
        resource_id = tool.resource_id
        resource = model.get_resource(resource_id)
        return render.view_tool(tool, resource, session=session)


class IndexToolSoftware(object):
    def GET(self):
        tools = list(model.get_tool_software())
        return render.index_tool(tools, session=session)


class IndexToolBook(object):
    def GET(self):
        tools = list(model.get_tool_book())
        return render.index_tool(tools, session=session)


class IndexToolAI(object):
    def GET(self):
        tools = list(model.get_tool_ai())
        return render.index_tool(tools, session=session)


class IndexToolDL(object):
    def GET(self):
        tools = list(model.get_tool_dl())
        return render.index_tool(tools, session=session)