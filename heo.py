from flask import Flask, render_template,request
from datetime import datetime



app = Flask(__name__)

time = datetime.utcnow()
time = time.strftime('%Y-%m-%d %H:%M:%S')




class User:
    def __init__(self, username , password):
        self.username = username
        self.password = password


def login(func):
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        password = request.args.get('password')
        print(username)
        print(password)
        id =1234
        passw = '1234'

        if username==id and password==passw:
            return 'login success'
        else:
            return 'failed'
    return wrapper

@app.route('/' ,methods=['POST'])
@login
def hello():
    return 'hi'

if __name__ == '__main__':
    app.run()