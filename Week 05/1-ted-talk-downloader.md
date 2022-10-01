# Automated TED Talk Downloader

## Importing the libraries

```python
import requests
from bs4 import BeautifulSoup 
import re
import sys
```

## Automated custom code

```python
url = input("Please Enter Your Ted Talk URL : ")
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
next_data_script = soup.find(id="__NEXT_DATA__")

data_json = next_data_script.string
player_data = json.loads(data_json)['props']['pageProps']['videoData']['playerData']
url_content = json.loads(player_data)['resources']['h264'][0]['file']
print(url_content)
mp4_response = requests.get(url_content)

user_name = input("Please enter file name: ")

file_name = user_name+'.mp4'
with open(file_name,'wb') as f:
    f.write(mp4_response.content)
```

## Automated video code

```python
import requests 
from bs4 import BeautifulSoup 
import re 
import sys 

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")


url = input("Please Enter Your Ted Talk URL : ")
req = requests.get(url)

soup = BeautifulSoup(req.content, features="lxml")
result=''
for val in soup.findAll("script"):
    if(re.search("resources",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
result_mp4=result_mp4+'mp4'
mp4_url = result_mp4.split('"')[0]

print("Downloading video from : " + result_mp4)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in: " + file_name)

req = requests.get(mp4_url)

user_name = input("Please enter file name: ")
file_name = user_name+'.mp4'
with open(file_name,'wb') as f:
    f.write(req.content)
```

