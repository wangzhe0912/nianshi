#-*- coding: UTF-8 -*-
"""
Created on 2017年1月25日

@author: wangzhe12
描述：用于将txt文档转换为HTML文档
"""
from language_format import get_html_text

def trans_txt_to_html(txt):
    result = ""
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
            result += get_html_text(script, language_suffix)
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
    

if __name__ == '__main__':
    txt = open('C:\\Users\\wangzhe12\\Desktop\\test.txt','rb')
    print trans_txt_to_html(txt)
    