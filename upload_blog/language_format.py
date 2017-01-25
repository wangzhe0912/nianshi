#-*- coding: UTF-8 -*-
"""
Created on 2017年1月25日

@author: wangzhe12
描述：
该模块的作用是将各种语言的输入转换为带有CSS样式的HTML字符串
"""
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename


def get_html_text(plain_text, language_suffix):
    #formatter = HtmlFormatter(encoding='utf-8', style = 'emacs', linenos = True)
    formatter = HtmlFormatter(encoding='utf-8', style = 'emacs', linenos = True)
    lexer = get_lexer_for_filename('a.' + language_suffix.lower())
    return highlight(plain_text, lexer, formatter)
    
if __name__ == '__main__':
    script = """
print 1+1
def func(a):
    print a*2
    """
    language_suffix = 'py'
    print get_html_text(script, language_suffix)
