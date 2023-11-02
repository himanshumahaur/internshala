import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "scheme": "https",
    "host": "www.amazon.in",
    "filename": "/s",
    "query": {
        "k": "bags",
        "crid": "24FPAHKFT7AM5",
        "sprefix": "bags,aps,228",
        "ref": "nb_sb_noss_1"
    },
    "remote": {
        "Address": "52.84.11.190:443"
    },
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'
}


base_url = "https://www.amazon.in/s?k=bags&crid=24FPAHKFT7AM5&sprefix=bags%2Caps%2C228&ref=nb_sb_noss_1"
num_pages = 20

url = f"{base_url}&page={1}"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)


# for page_number in range(1, num_pages + 1):
#     page_url = f"{base_url}&page={page_number}"

#     response = requests.get(page_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
