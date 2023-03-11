from bs4 import BeautifulSoup
from auth import html


#with open('Gaijin Market.html') as html_file:
soup = BeautifulSoup(html, 'html.parser')

# define an empty array to store the divs with the desired class and their spans with desired class
vehicles_array = []

# loop through all the divs in the HTML document that have the desired class (e.g. 'my-class')
for div in soup.find_all('div', class_='lot'):

    name = div.find('div', class_='name')
    if name is not None:
        
          
        
        for span in div.find('span', class_='price'):
            price = span.text

   
        vehicles_array.append([name.text, price])

print(vehicles_array)

