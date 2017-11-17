from flask import Flask

app = Flask(__name__)


# 将函数index注册为应用根url的处理程序：
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 添加一个动态路由：
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


# 启动Flask集成的开发Web服务器：
if __name__ == '__main__':
    app.run(debug=True)
