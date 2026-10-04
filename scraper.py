from bs4 import BeautifulSoup
import requests


URL = 'https://appbrewery.github.io/Zillow-Clone/'


def get_data():
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find('ul', class_='List-c11n-8-84-3-photo-cards')

    if listings is None:
        raise ValueError('Could not find the listings container on the page.')
    items = listings.find_all('article', class_='StyledPropertyCard-c11n-8-84')
    items_data = []
    for item in items:
        link = item.find('a')['href']
        price = item.find('span', class_='PropertyCardWrapper__StyledPriceLine').get_text(strip=True)
        clean_price = price.split('+')[0].split('/')[0].strip()
        address = item.find('address').get_text(strip=True)
        address = ' '.join(address.split())
        address = address.replace(' | ', ', ')
    
        items_data.append({
            'link': link,
            'price': clean_price,
            'address': address
        })
    

    return items_data
