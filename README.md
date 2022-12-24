# algorithm-server

1. api

2. rpc 

3. websocket


rpc 调用服务端函数，内含向服务器传送数据，服务器计算后向client返回数据

rpc , api 都是网络函数

sdk是把网络函数封装好, 可以是多语言版本的，python版本的，nodejs版本的，利用的都是所在语言的访问api的库，都有request库

访问api的方法： 1、浏览器、postman 2、curl命令行 3、类似python requests库, node.js中有(import fetch from 'node-fetch')

创建api的库Flask，创建的api可以返回json，也可以在浏览器返回html页面

