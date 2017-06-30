# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from new_file import get_data
app = Flask(__name__)



@app.route('/content', methods=['POST'])
def show_content() -> 'html':
    month = request.form['month']
    day = request.form['day']
    results = get_data(month,day)
    return render_template('results.html',
                            the_results=results,
                           )






@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""

    return render_template('entry.html',

                           the_title='历史上的今天')



if __name__ == '__main__':

    app.run(debug=True)
