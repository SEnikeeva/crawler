from urllib.request import urlopen, Request
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests


def save_links_from_site(soup, urls_path='index.txt', start_idx=0):
    links = []
    for h3 in tqdm(soup.findAll('h3')):
        if h3['class'][0] != 'gs_rt':
            continue
        curr_l = h3.find('a').get('href')
        if not (curr_l is None) and (len(curr_l) > 1) and ('/' in curr_l):
            links.append(curr_l)
    end_idx = start_idx
    with open(urls_path, 'a') as file:
        for i, h3 in enumerate(set(links)):
            file.write(f"{end_idx}. " + h3 + '\n')
            end_idx += 1
    return end_idx


def get_urls(urls_path='index.txt'):
    urls = []
    with open(urls_path, 'r') as file:
        for line in file:
            urls.append(line.split()[1])
    return urls


def main():

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    links = ['https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q=self+supervised+learning&oq=self+supervised+lea',
             'https://scholar.google.com/scholar?start=10&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=20&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=30&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=40&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=50&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=60&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=70&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=80&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=90&q=self+supervised+learning&hl=ru&as_sdt=0,5',
             'https://scholar.google.com/scholar?start=100&q=self+supervised+learning&hl=ru&as_sdt=0,5']
    end_idx = 0
    for i, link in enumerate(links):
        req = Request(url=link, headers=headers)
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        end_idx = save_links_from_site(soup, start_idx=end_idx)

    urls = get_urls()
    for i, url in tqdm(enumerate(urls)):
        r = requests.get(url)
        with open(f'pages/{i}.txt', 'w') as file:
            file.write(r.text)


if __name__ == '__main__':
    main()
