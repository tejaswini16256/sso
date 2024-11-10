from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <h2>Login Form</h2>
                <form action="/login" method="post">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username"><br><br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password"><br><br>
                    <input type="submit" value="Login">
                </form>
            </body>
        </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username  and password :
        return f"<h1>Welcome, {username}!</h1>"
    else:
        return "<h1>Invalid credentials. Please try again.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
