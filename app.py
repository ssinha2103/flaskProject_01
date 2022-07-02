from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/oddeven/<int:num>')
def pairity_check(num):
    if (num % 2) == 0:
        result = {"pairity": "Even"}
    else:
        result = {"pairity": "Odd"}
    return jsonify(result)
    #return result



if __name__ == '__main__':
    app.run()
