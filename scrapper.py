from stack import extract_from_stack
from wework import extract_from_wework
from remoteok import extract_from_remoteok
from make_csv import save_to_csv


def make_url(word):
    resource = ["https://stackoverflow.com/jobs?r=true&q={}",
                "https://weworkremotely.com/remote-jobs/search?term={}",
                "https://remoteok.io/remote-dev+{}-jobs",
                ]
    urls = []
    for i in resource:
        url = i.format(word)
        urls.append(url)
    return urls


def job_scrapper(word):
    total = []
    url_list = make_url(word)
    total.extend(extract_from_stack(url_list[0]))
    total.extend(extract_from_wework(url_list[1]))
    total.extend(extract_from_remoteok(url_list[2]))
    return total
