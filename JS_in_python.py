#coding:utf-8
#python.__version__=2.7.14


#PyExecJs执行单个函数，python 2.7/python 3.6
import execjs
from js_content import js,js2
sss='kfj\r\nlhss '
#执行一个函数的写法
p1=execjs.compile(js)
s1=p1.call('encode',sss)
print('PyExecJs执行结果(encode): ',s1)

#执行一个类的写法
p2=execjs.compile(js2)
s2=p2.call('new Base64().encode',sss)
print('PyExecJs执行结果(new Base64()): ',s2)

p2=execjs.compile(js2+'var base=new Base64();')
s2=p2.call('base.encode',sss)
print('PyExecJs执行结果(base.encode): ',s2)



#以下是pyV8方法，执行单个函数，python 2.7
# import PyV8
# ctxt=PyV8.JSContext()
# ctxt.enter()
# ctxt.eval(js2+'var base=new Base64();')
# encode=ctxt.locals.base.encode
# print('PyV8执行结果: ',encode(sss))
