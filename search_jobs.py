import requests
from bs4 import BeautifulSoup

def search_jobs(query):
    urls = [
        "https://www.google.com/search?q=remote+python+jobs",
        "https://www.bing.com/search?q=remote+python+jobs",
        "https://duckduckgo.com/html/?q=remote+python+jobs"
    ]
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("a", {"class": "result__url"})
        for job in jobs:
            if query.lower() in job.text.lower():
                print(job.text.strip())
                print(job["href"])
                print("-" * 80)

search_jobs("remote python")
