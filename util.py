# -*- coding: UTF-8 -*-
import traceback
import StringIO
def error():
    fp = StringIO.StringIO()    #创建内存文件对象
    traceback.print_exc(file=fp)
    return fp.getvalue()