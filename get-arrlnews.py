#KTD 12/11/2020
#last update: 3/16/23
#Scrape the ARRL NEWS site for the latest audio broadcast, and download it
#Destination file to be read and written is passed as the first (and only) argument with full path.
#Not sure when or how often this podcast is published.
import requests, feedparser
import sys

rss_url = 'https://feeds.blubrry.com/feeds/arrlaudionews.xml'
feed = feedparser.parse( rss_url )
audio_url = feed.entries[0].enclosures[0].href
url_text_file = sys.argv[1]

#print(audio_url)
#audio_file = requests.get(audio_url)

with open(url_text_file, 'r+') as arrlfile:
    last_url = arrlfile.read()
    #print('last url: '+last_url)
    arrlfile.seek(0)
    if audio_url != last_url:
        arrlfile.write(audio_url)
        #print('writing new audio url')
    else:
        arrlfile.write(' ')
    #print('writing a single space')
    arrlfile.truncate()
    arrlfile.close()

# end of code
