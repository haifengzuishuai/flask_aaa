# encoding:utf-8
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'hallow haifeng!'


@app.route('/login', methods=['post','get'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        print(name)
        print(password)
        if name == '1' and password == '1':
            return redirect(url_for('index'))
        else:
            return render_template('login.html')


@app.route('/catalogue')
def catalogue():
    return '返回所有的博客内容'


@app.route('/catalogue/<id>')
def article(id):
    return '您请求的文章是%s' % id


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=5000 ,debug=True)
