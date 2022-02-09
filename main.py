from urllib.request import urlopen
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests


def save_links_from_site(soup, urls_path='links.txt'):
    links = []
    curr_l = None
    for link in tqdm(soup.findAll('a')):
        try:
            curr_l = link.get('href')
            if not (curr_l is None) and (len(curr_l) > 1) and ('/' in curr_l):
                curr = curr_l.split('/')
                if (len(curr) == 2) and curr_l[1].isupper():
                    links.append(curr_l)
        except:
            print('exception' + 'in' + curr_l)

    with open(urls_path, 'w') as file:
        for link in set(links):
            file.write(link)


def get_urls(urls_path='links.txt'):
    urls = []
    with open(urls_path, 'r') as file:
        for line in file:
            urls.append(line)
    return urls


def main():
    link = 'https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q=self+supervised+learning&oq=self+supervised+lea'
    page = urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    save_links_from_site(soup)

    # urls = get_urls()
    # for i, url in enumerate(urls):
    #     r = requests.get(url)
    #     with open(f'pages/page_{i}', 'w') as file:
    #         file.write(r.text)


if __name__ == '__main__':
    main()

