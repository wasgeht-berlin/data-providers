from bs4 import BeautifulSoup
import urllib
import json
import time
from datetime import datetime
import hashlib

url = "http://www.karreraklub.de/karrera/termine/liste"
page = urllib.urlopen(url).read()

soup = BeautifulSoup(page)

events = soup.findAll('div', class_='termin_content')

result = []

for event in events:
    date_text = event.find('span', class_='termin_info_datum').text
    time_text = event.find('span', class_='termin_info_uhrzeit').text

    ts = time.strptime(date_text[4:] + ' ' + time_text, '%d.%m.%Y %H:%M')  
    starting_time = datetime.fromtimestamp(time.mktime(ts)).isoformat()

    location = event.find('span', class_='termin_info_ort').text

    title = event.find('span', class_='termin_info_name').text
    description = event.find('div', class_='termin_live_info_text').text

    tags = ['party']

    if title.find('Konzert') > 0:
        tags.append('concert')

    result.append({ 
        'starting_time': starting_time, 
        'location': { 'human_name': location }, 
        'title': title,
        'description': description,
        'hash': hashlib.sha1(starting_time + location).hexdigest(),
        'url': url, # TODO: This may need a little refinement,
        'tags': tags
    })

print(json.dumps(result, indent=4))
