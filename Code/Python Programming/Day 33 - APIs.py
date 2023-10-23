import requests, smtplib, time
from tkinter import *
import datetime as dt


### Exercise 1 ###
def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    canvas.itemconfig(cns_quote, text=quote)

window = Tk()
window.title('Kanye Says...')
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file='../Data/33/background_33.png')
canvas.create_image(150, 207, image=bg_image)
cns_quote = canvas.create_text(150, 207, font=('Ariel', 20), width=250, text='', fill='white')
canvas.pack()

button = Button()
btn_image = PhotoImage(file='../Data/33/kanye_33.png')
button.config(image=btn_image, command=get_quote)
button.pack()


window.mainloop()


### Project ###
MY_LAT = 9.076479
MY_LONG = 7.398574
EMAIL = ' '
PASSWRD = ' '

def is_dark():
    sun_url = 'https://api.sunrise-sunset.org/json'
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    response = requests.get(url=sun_url, params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    current_hour = dt.datetime.now().hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True

def is_iss():
    iss_url = 'http://api.open-notify.org/iss-now.json'
    response_1 = requests.get(url=iss_url)
    response_1.raise_for_status()

    data_1 = response_1.json()
    longitude = float(data_1['iss_position']['longitude'])
    latitude = float(data_1['iss_position']['latitude'])

    if (MY_LONG-5) <= longitude <= (MY_LONG+5) and (MY_LAT-5) <= latitude <= (MY_LAT+5):
        return True

while True:
    time.sleep(60)
    if is_dark() and is_iss():
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWRD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg='Subject:Look Up☝️\n\nThe ISS is passing your location')
