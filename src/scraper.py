import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.minecraftcrafting.info/'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

data = []

for row in table.find_all('tr'):
    columns = row.find_all('td')
    
    if columns:
        image_name = columns[0].text.strip()
        
        image_tag = row.find('img')
        image_file_name = image_tag['src'].split('/')[-1] if image_tag else None
        
        if image_file_name is None:
            continue

        data.append({
            'image_name': image_name,
            'image_file_name': image_file_name
        })

data = data[2:]
json_data = json.dumps(data, indent=4)

path = 'images_data.json'

with open(path, 'w') as json_file:
    json_file.write(json_data)

print("JSON data has been saved at", path)

