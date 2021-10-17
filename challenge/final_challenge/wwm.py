
import requests
from bs4 import BeautifulSoup





def extract_job(html):
  title = html.find("a", recursive = False).find("span", {"class":"title"}).get_text(strip=True)
  
  company = html.find("a", recursive = False).find("span", {"class":"company"}).get_text(strip=True)

  link = html.find("a", recursive = False)["href"]

 
  return {
    'title': title, 
    'company': company, 
    'link': f"https://weworkremotely.com{link}"
    }



def extract_jobs(url):
  jobs = []
 
  print("Scrapping WWM")
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("div", {"class": "jobs-container"}).find_all("li", {"class": "feature"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs  


def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs




  