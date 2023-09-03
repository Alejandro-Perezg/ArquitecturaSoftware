from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods = ['POST','GET'])
def loginCheck():
    username = request.form['username']
    password = request.form['password']

    if username == username.capitalize() and password.isalnum():
        return render_template('success.html')
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
    