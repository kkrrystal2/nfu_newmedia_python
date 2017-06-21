# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request, escape
from today_in_history_4web import get_weather, get_form

app = Flask(__name__)


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
