import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url: str) -> dict:
    product_details = {}

    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features='lxml')