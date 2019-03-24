# coding: utf8

from flask import Flask
 
app = Flask(__name__)

@app.route("/list/<int:number>")
def bootstrap(number):
    data = [i for i in range(number)]
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <div>{}</div>
                </html>'''.format(data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')