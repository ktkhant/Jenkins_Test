from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! update 1.9"

if __name__ == '__main__':
    app.run(debug=True)
