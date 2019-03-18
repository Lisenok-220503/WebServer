# coding: utf8

from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"

@app.route('/image_sample')
def image():
    return '''<img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/сова.jpg'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')