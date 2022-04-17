from cgitb import html
from itertools import product
from bs4 import BeautifulSoup
import  requests

url = "https://www.flipkart.com/cameras/pr?sid=jek,p31"

response = requests.get(url)
# print(response.status_code)
# print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.find(id="next-page-link-tag"))

# code to extract ahref
# for link in soup.find_all('a'):
#     print(link.get('href'))

# code to extract images
# for image in soup.find_all('img'):
#     print(image.get('src'))

# code to extract data on basis of class
# product = soup.find_all('div', class_='_3pLy-c row')
# print(product)

# product = soup.find('div', attrs={'class':'_3pLy-c row'})
# print(product)