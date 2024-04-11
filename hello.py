from flask import Flask
from flask import request

from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1> Hello %s </h1> ' % user.name


@app.route('/redirect')
def indexre():
    return redirect('https://www.sapat.com/')


@app.route('/cookie')
def home():
    response =  make_response('<h1>This document carries a cookies ! </h1>')
    response.set_cookie('answer','42')
    return response

@app.route('/browser')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your Browser is %s</h1>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1> Hii , %s Wecome to sapat</h1>'% name



if __name__ == '__main__':
    app.run(debug=True)