#KTD 12/11/2020
#last update: 3/16/23
#Scrape the Amateur Radio Newsline site for the latest audio broadcast, and download it
#Destination file to be read and written is passed as the first (and only) argument with full path.
#They usually publish every Friday morning.
import requests
import sys
from bs4 import BeautifulSoup

URL = 'https://www.arnewsline.org'
page = requests.get(URL)
url_text_file = sys.argv[1]
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='page')

#print(results.prettify())

tag = results.find('div', class_='sqs-audio-embed')
audio_url = tag.attrs.get('data-url')
#print('audio url: '+audio_url)

with open(url_text_file, 'r+') as arnfile:
    last_url = arnfile.read()
    #print('last url: '+last_url)
    arnfile.seek(0)
    if audio_url != last_url:
        arnfile.write(audio_url)
        #print('writing new audio url')
    else:
        arnfile.write(' ')
        #print('writing a single space')
    arnfile.truncate()
    arnfile.close()
