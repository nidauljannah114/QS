from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('login', methods= ('GET', 'POST'))
def login():
    return 'index'

@app.route('/login')
def login():
    print(request)
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


'''
Create = Post
Read = GET
Update = PUT
Delete = DELETE
'''