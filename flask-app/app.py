from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/login')
def login_mask():
    return '<h2>Login</h2>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')