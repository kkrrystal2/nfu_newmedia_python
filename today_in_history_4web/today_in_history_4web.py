# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape, url_for, send_file

app = Flask(__name__)

with open ('today_in_history_4web','r',encoding='utf8')as data:
    date=data.readlines()
data_all=[]
for item in date:
    item_data = item.strip().split(' ')
    item_dict = {x.split(':')[0]:x.split(':')[1] for x in item_data}
    data_all.append(item_dict)

date_list=[x['日期'] for x in data_all]

@app.route('today_in_history_4web', methods=['POST'])

def do_search() -> 'html':

    """Extract the posted data; perform the search; return results."""

    date=request.form['date']

    title = '以下是您的结果：'
    results = get_img(date)
    return render_template('results.html',
                           the_title=title,
                           the_city=date,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='历史上的今天查询！',
						   the_user_date=date_list)

						   
#这里我们接受一个 filename 檔名变量，http://127.0.0.1:5000/img/檔名
@app.route('/maps/<filename>')  #filename
def get_image(filename):        #filename 
    #傳送mimetype="image/"
    #假定都是image/png格式



    import os.path
    
    return send_file(os.path.join("maps",filename), mimetype='image/png')

if __name__ == '__main__':

    app.run(debug=True)
