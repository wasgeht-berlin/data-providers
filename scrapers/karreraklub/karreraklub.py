from bs4 import BeautifulSoup
import urllib
import json
import time
import datetime

url = "http://www.karreraklub.de/karrera/termine/liste"
page = urllib.urlopen(url).read()

soup = BeautifulSoup(page)

events = soup.findAll('div', class_='termin_info')

result = []

for event in events:
    date_text = event.find('span', class_='termin_info_datum').text
    time_text = event.find('span', class_='termin_info_uhrzeit').text

    ts = time.strptime(date_text[4:] + ' ' + time_text, '%d.%m.%Y %H:%M')  
    starting_time = datetime.datetime.fromtimestamp(time.mktime(ts)).isoformat()

    location = event.find('span', class_='termin_info_ort').text

    title = event.find('span', class_='termin_info_name').text

    description = ''

    full_name = event.find_all('span', class_='termin_info_name')
    for part in full_name:
        description += part.text + '\n'

    bands = event.find_all('span', class_='termin_info_live')
    for band in bands:
        description += band.text #+ ' ' + band.next_element.text + '\n'

    result.append({ 
        'starting_time': starting_time, 
        'human_location_name': location, 
        'title': title,
        'description': description
    })

print(json.dumps(result, indent=4))
