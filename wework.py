import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'


def get_soup(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def extract_from_wework(url):
    data = []
    soup = get_soup(url)
    jobs = soup.find_all("section", {"class": "jobs"})
    for job in jobs:
        lists = job.find_all("li", {"class": "feature", "class": ""})
        for list in lists:
            a = list.find("a")
            href = a.get("href")
            company = a.find("span", {"class": "company"})
            title = a.find("span", {"class": "title"})
            try:
                data.append([title.contents[0], company.contents[0],
                             f"https://weworkremotely.com{href}"])
            except AttributeError:
                pass

    return data


# print(extract_from_wework(
#     "https://weworkremotely.com/remote-jobs/search?term=javascript"))
