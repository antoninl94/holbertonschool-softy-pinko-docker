from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_route():
    return redirect('/api/hello')

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
