import requests, json

def get_data(month,day):
        contents=[]
        url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=11&day=1".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=1".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=2".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=3".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=4".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=5".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=6".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=7".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=8".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=9".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=10".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=11".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=12".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=13".format(month,day))
		url=("http://api.juheapi.com/japi/toh?key=1a21b2aace47c4fc71c446f7b025fe47&v=1.0&month=1&day=14".format(month,day))
        import requests
        r = requests.get(url)
        data=r.json()
        results=data['result']
        #print(results[:5]) +each_i['title']+each_i['des']
        for each_i in results[:5]:#打印其标题及其梗概
           contents.append(str(each_i['month'])+'月'+str(each_i['day'])+'日'+each_i['title']+each_i['des'])
        return contents
