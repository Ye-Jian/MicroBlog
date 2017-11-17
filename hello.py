from flask import Flask

app = Flask(__name__)


# 将函数index注册为应用根url的处理程序：
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 启动Flask集成的开发Web服务器：
if __name__ == '__main__':
    app.run(debug=True)
