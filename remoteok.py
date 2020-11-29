import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'


def get_soup(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def extract_from_remoteok(url):
    data = []
    soup = get_soup(url)
    tds = soup.find_all(
        "td", {"class": "company position company_and_position"})
    for td in tds:
        try:
            a = td.find("a", {"class": "companyLink"})
            href = a.get('href')
            company = a.find("h3").string
            title = td.find("h2").string
            data.append([title, company, f"https://remoteok.io{href}"])
        except AttributeError:
            pass

    return data

   # return extract_jobs(urls)
# print(extract_from_wework("https://remoteok.io/remote-dev+javascript-jobs"))
