# Automated Emailing of Top News Stories Using BS4

```python
# Importing the libraries
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Setting the current date and time
now = datetime.datetime.now()
content = ''
cnt = ''

# Requesting the top news stories
url = 'https://news.ycombinator.com/'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

# Parsing the HTML tags
cnt +=('<b>Hacker News Top Stories :</b>\n'+'<br>'+'-'*50+'<br>')
for i,tag in enumerate(soup.find_all("span", class_="titleline")):
    cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
    
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Email')

# Writing the email
print('Composing Email...')
recipients=['your@gmail.com']
SERVER = 'smtp.gmail.com' 
PORT = 587 
FROM =  'your@gmail.com' 
TO = ', '.join(recipients) 
PASS = '****'

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

# Sending the email
print('Initiating Server')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email has been sent successfully.')

server.quit()

```
