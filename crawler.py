import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_links():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select(
        'body > h3 > a'
    )
    data = []
    for title in my_titles:
        data.append(title.get('href'))

    print(data)

    return data

def get_content(link):
    abs_link = 'https://beomi.github.io' + link
    req = requests.get(abs_link)
    html = req.text
    soup = bs(html, 'html.parser')

    print(soup.select('h1')[0].text)


def get_data():
    get_content()

if __name__ == '__main__':
    start_time = time.time()

    pool = Pool(processes=4)
    pool.map(get_content, get_links())

    finish_time = time.time()
    elapsed_time = finish_time - start_time

    print(elapsed_time)
