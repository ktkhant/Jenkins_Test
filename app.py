from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! update 1.7"

if __name__ == '__main__':
    app.run(debug=True)
