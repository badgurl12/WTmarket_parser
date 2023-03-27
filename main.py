from bs4 import BeautifulSoup
from auth import stripHTML

#with open('Gaijin Market.html') as html_file:
soup = BeautifulSoup(stripHTML(), 'html.parser')

# define an empty array to store the divs with the desired class and their spans with desired class
vehicles_array = []

# loop through the document finding prices
def find_sell_prices():

    for div in soup.find_all('div', class_='lot inventory'):

        name = div.find('div', class_='name')
        price_span = div.find('span', class_='price')

        if name is not None and price_span is not None:
            price = price_span.text
            vehicles_array.append([name.text, price])

find_sell_prices()

print(vehicles_array)
