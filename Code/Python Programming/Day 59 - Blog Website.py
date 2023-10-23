from flask import Flask, render_template, request
import requests, smtplib


response = requests.get(url='https://api.npoint.io/3c821def64f64845bdf0')
response.raise_for_status()
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', post=all_posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', success=False)
    elif request.method == 'POST':
        data = request.form
        send_mail(data)
        return render_template('contact.html', success=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:num>')
def post(num):
    return render_template('post.html', blog_number=num, post=all_posts)


def send_mail(form):
    name = form['name']
    email = form['email']
    phone_number = form['phone-number']
    message = form['message']
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(from_addr='', to_addrs='', msg=f'Subject: Message from Website\n\nName: {name}\nEmail: {email}\n Phone Number {phone_number}\Message: {message}')


if __name__ == '__main__':
    app.run(debug=True)