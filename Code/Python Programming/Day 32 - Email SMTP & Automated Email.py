import datetime as dt
import smtplib, random
import pandas

EMAIL = ''
PASSWD = ''
PLACEHOLDER = '[NAME]'

### Exercise 1 ###
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWD)
    connection.sendmail(from_addr=EMAIL, to_addrs='', 
                        msg='Subject:Hello\n\nThis is the body of my email')


## Exercise 2 ###
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=8, day=31)
print(date_of_birth)


### Project 1 ###
current_dt = dt.datetime.now()
current_weekday = current_dt.weekday()

if current_weekday == 0:
    with open('../Data/32/quotes_32.txt') as f:
        quotes_list = f.readlines()
        message = random.choice(quotes_list)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL, to_addrs='', 
                            msg=f'Subject:Motivational Quote\n\n{message}')


### Project 2 ###
###### UPDATING CSV ######
info_dict = {
    'name': ['Test', 'Ben'],
    'email': ['', ''],
    'year': ['1995', '1985'],
    'month': ['9', '9'],
    'day': ['4', '5'],
}

bd_message = pandas.read_csv('../Data/32/birthdays_32.csv')
data = bd_message.to_dict(orient='records')
for dict in data:
    new_data = {key:info_dict[key] for (key, value) in dict.items()}
new_data_df = pandas.DataFrame(new_data)

###### CHECKING IF BIRTHDAY MATCH WITH CURRENT DATETIME ######
current_dt = dt.datetime.now()
current_month = current_dt.month
current_day = current_dt.day
for index, row in new_data_df.iterrows():
    month = int(row['month'])
    day = int(row['day'])
    name = row['name']
    to_email = row['email']

    if month == current_month and day == current_day:
###### REPLACING PLACEHOLDER NAME ######
        with open(f'../Data/32/letter_{random.randint(1, 3)}_32.txt') as f:
            text = f.read()
            new_text = text.replace(PLACEHOLDER, name)
###### SENDING EMAIL ######
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWD)
            connection.sendmail(from_addr=EMAIL, to_addrs=to_email,
                                msg=f'Subject:Birthday Wishes!\n\n{new_text}')

