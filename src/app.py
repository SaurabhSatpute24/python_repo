from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# @app.route("/")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Login Successful!'
        else:
            return 'Login Failed!'
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
