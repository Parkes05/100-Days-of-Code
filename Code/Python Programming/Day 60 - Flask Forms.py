from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_60.html')

@app.route('/login', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'<h1>Name: {username}, Password: {password}</h1>'
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)