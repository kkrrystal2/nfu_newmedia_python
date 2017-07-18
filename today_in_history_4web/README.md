today_in_history_4web




# 简介 
根据你所输入的日期,查询输入的这一天历史上发生的大事件(选取前五件事情)


		

## 输入：
日期（月、日）
上行输入月份
下行输入日期
## 输出：
用户得到输出结果为：历史上的某一天发生了什么(选取前五件事情)
## 从输入到输出，本组作品使用了：
### 模块
* [request](http://www.python-requests.org/en/master/)  
* [Flask](http://www.pythondoc.com/flask/)

### 数据
* [聚合数据](https://www.juhe.cn/)




### API
* [聚合数据 历史上的今天](http://api.juheapi.com/japi/toh?key=4bc027ace0535ecf7e935870a1b9deef&v=1.0&month=11&day=1) 限量访问100次


## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 today_in_history_4web.py  启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：[ today_in_history_4web.py ]today_in_history_4web.py ) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"或"date"，变数名称(name)为'date'，[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「查询」，则产生新的web 请求，按照form元素中定义的method='POST' action='/content'，以POST为方法，动作为today_in_history_4web的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/content', methods=['POST'])的函数 weather_forecast() 

7. [today_in_history_4web.py ](today_in_history_4web.py ) 中 today_in_history_4web() 函数，把用户提交的数据，以flask 模块request.form['date']取到Web 请求中，HTML表单变数名称日期的值，使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出）。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，显示
 信息



## 作者成员：
见[_team_.tsv](https://github.com/kkrrystal2/nfu_newmedia_python/blob/master/_team_.tsv)

