
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(html):
  title = html.find("td", {"class" : "company_and_position"}).find("a",recursive = False).find("h2").get_text(strip=True)

  company = html["data-company"]
  
  job_id = html["data-id"]

  return {
    'title': title, 
    'company': company, 
    'link': f"https://remoteok.io/remote-jobs/{job_id}"
    }



def extract_jobs(url):
  jobs = []
  print("Scrapping RO")
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class": "job"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs  


def get_jobs(word):
  url = f"https://remoteok.io/remote-{word}-jobs"
  jobs = extract_jobs(url)
  return jobs



  