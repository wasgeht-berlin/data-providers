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
    description = ''

    djs = event.find_all('span', class_='termin_info_djs')
    for dj in djs:
        description += dj.text + dj.next_sibling.text

    bands = event.find_all('span', class_='termin_info_live')
    bands = [band.text + band.next_sibling.text for band in bands]

    if len(bands) > 0:
        title = ', '.join(bands) + ' - ' + title
        
        description_tag = event.find('div', class_='termin_live_info_text')
        description_tag.find('span').decompose()

        description = description_tag.text.lstrip('\n\t')
    
    aname = event.find('span', class_='termin_info_datum').parent['name']

    tags = ['Party']

    if title.find('Konzert') > 0:
        tags.append('Concert')

    result.append({ 
        'starting_time': starting_time, 
        'location': { 'human_name': location }, 
        'title': title,
        'description': description,
        'hash': hashlib.sha1(starting_time + location).hexdigest(),
        'url': url + '#' + aname, 
        'tags': tags
    })

print(json.dumps(result, indent=4))
