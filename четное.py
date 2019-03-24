# coding: utf8

from flask import Flask, request, render_template
 
app = Flask(__name__)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')