import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_yacht_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    yachts = []
    listings = soup.find_all('div', class_='listing')  # rnek selector
    for item in listings:
        name = item.find('h2').text
        price = item.find('span', class_='price').text
        year = item.find('span', class_='year').text
        yachts.append({'name': name, 'price': price, 'year': year})

    return pd.DataFrame(yachts)

if __name__ == "__main__":
    url = 'https://example-yacht-site.com/listings'
    df = scrape_yacht_data(url)
    df.to_csv('../data/yachts_raw.csv', index=False)
    print("Data collected and saved to data/yachts_raw.csv")

