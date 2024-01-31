from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_get():
    return '<h1>Hello, World v5!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
