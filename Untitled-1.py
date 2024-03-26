import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.bongthom.com/'
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements on the webpage based on HTML tags, classes, or IDs
# For example, let's extract all the links (anchor tags) from the webpage
links = soup.find_all('a')

# Print the text and URLs of the extracted links
for link in links:
    print(link.text.strip(), ':', link['href'])
