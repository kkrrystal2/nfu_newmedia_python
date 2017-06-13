import urllib.request, json

def get_history(date):
    print ('''
    ************************************************
         Welcome to today_in_history System!       
    ************************************************''')
    try:
        with open('date.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if date in line:
                    date_code = line.split('=')[0].strip()
        #历史上的今天api            
        url = (http://api.juheapi.com/japi/toh?key=您申请的KEY&v=1.0&month=11&day=1.format(code=date_code))

        response = urllib.request.urlopen(url)
        today_in_history_html = response.read()
        json_data = json.loads(today_in_history_html)
        #print(json_data)
     
            
     return(_id,title,pic,year,month,day,des,lunar,)

    except NameError :
        print('不存在此日期')
