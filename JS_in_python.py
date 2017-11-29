#coding:utf-8
#python.__version__=2.7.14


#PyExecJs执行单个函数，python 2.7/python 3.6
import execjs
from js_content import js
sss='kfj\r\nlhss '
p=execjs.compile(js)
s=p.call('encode',sss)
print('PyExecJs执行结果: ',s)




#以下是pyV8方法，执行单个函数，python 2.7
# import PyV8
# ctxt=PyV8.JSContext()
# ctxt.enter()
# ctxt.eval(js)
# encode=ctxt.locals.encode
# print('PyV8执行结果: ',encode(sss))
