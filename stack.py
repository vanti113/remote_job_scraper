import requests
from bs4 import BeautifulSoup


s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'


def get_soup(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def extract_jobs(urls):
    data = []
    for url in urls:
        soup = get_soup(url)
        a_links = soup.find_all("a", {"class": "s-link stretched-link"})
        # for a in a_links:
        h3_links = soup.find_all("h3", {"class": "fc-black-700 fs-body1 mb4"})
        for a, h3 in zip(a_links, h3_links):
            title = a.get("title")
            company = h3.span.contents[0].strip()
            href = a.get("href")
            data.append(
                [title, company, f"https://stackoverflow.com/{href}"])

    return data


def extract_from_stack(url):
    urls = []
    soup = get_soup(url)
    pages = soup.find_all("a", {"class": "s-pagination--item"})
    for page in pages:
        href = page.get("href")
        urls.append(f"https://stackoverflow.com{href}")

    urls = set(urls)
    urls = list(urls)
    return extract_jobs(urls)
