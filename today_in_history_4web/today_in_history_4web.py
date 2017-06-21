# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)


import requests
r = requests.get('http://api.juheapi.com/japi/toh?key=4bc027ace0535ecf7e935870a1b9deef&v=1.0&month={m}&day={d}'format(m=month,d=day))
gg=r.text
aa= eval(gg)
aa['result'][0]['des']
len(aa['result'])
kkkf=[]
for i in range(len(aa['result'])):
    kki=aa['result'][i]['des']
    kkkf.append(kki)



@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    date = request.form['date']
    results = today_in_history
    return render_template('results.html',
                           the_results=results,
                           the_date = date,
                           the_history = results[1],

                           )



@app.route('/')

@app.route('/entry')

def entry_page() -> 'html':

    """Display this webapp's HTML form."""

    return render_template('entry.html',

                           the_title='历史上的今天')



if __name__ == '__main__':

    app.run(debug=True)
