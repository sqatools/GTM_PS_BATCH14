import requests
from bs4 import BeautifulSoup

url = input("Enter product page URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("p", class_="price_color").text

print(f"Price found: {price}")