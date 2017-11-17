from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


# 将函数index注册为应用根url的处理程序：
@app.route('/')
def index():
    return render_template('index.html')


# 添加一个动态路由：
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 启动Flask集成的开发Web服务器：
if __name__ == '__main__':
    manager.run()
