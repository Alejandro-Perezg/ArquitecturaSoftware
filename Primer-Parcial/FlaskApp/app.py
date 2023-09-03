from flask import Flask, request, jsonify
app = Flask(__name__)


# http://localhost:8081/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# http://localhost:8081/params?test=Mario
@app.route("/params", methods=["GET"])
def params():
    test = request.args.get("test", default="World", type=str)
    return f"Hello {test}"


# http://localhost:8081/name/mario
@app.route("/name/<name>", methods=["GET"])
def root(name: str):
    return f"Hello {name}"


@app.route('/test', methods=['POST'])
def my_view_func():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Hello {email}"


@app.route('/json', methods=["POST"])
def json():
    data = request.get_json()
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
