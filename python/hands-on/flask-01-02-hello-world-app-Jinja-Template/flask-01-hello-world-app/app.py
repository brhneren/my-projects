from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return "Neden size her yer Trabzon???"

@app.route('/third/subthird')
def third():
    return "Ne oldu simdi Trabzooon??"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True, port=2000)