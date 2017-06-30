# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from new_file import get_data
app = Flask(__name__)



@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    month_day = list(request.form['month_day'])
    month = month_day[0]
    day = month_day[1]
    results = get_data(month,day)
    return render_template('results.html',
                           the_results=results,

                           #the_history = results[1],

                           )

                           the_date = date,
                           the_history = results[1],)
>>>>>>> eba8f4a2a14ea7f5661ad328619401ef8fc37e33



@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""

    return render_template('entry.html',

                           the_title='历史上的今天')



if __name__ == '__main__':

    app.run(debug=True)
