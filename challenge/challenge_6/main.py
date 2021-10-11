

# [Challenge goals]
# 보일러플레이트를 사용하여 다음과 같은 프로그램을 만드세요.
# 알바천국 사이트 로 가서, 첫 페이지에 있는 슈퍼브랜드 채용정보의 회사들을 스크랩하세요.
# 각각 회사 페이지로 들어가서 알바 정보를 스크랩하세요.
# 회사 별로 스크랩 해온 알바 정보를 각각의 .csv 파일로 만들어 저장하세요.



import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"




def extract_job(company_url):
  jobs = []
  result = requests.get(company_url)
  soup = BeautifulSoup(result.text, "html.parser")
  trs = soup.find("div", {"id": "NormalInfo"}).find("tbody").find_all("tr")
  for tr in trs:
      tds = tr.find_all("td")
      if len(tds) != 5:
        continue
      else:  
        job = extract_job_data(tds)
        jobs.append(job)
  return jobs      
    


def extract_job_data(html):  
  place = html[0].get_text(strip=True).replace(u"\xa0",u" ")

  title = html[1].find("span",{"class":"title"}).string

  time = html[2].find("span",{"class":"time"})
  if time is None:
    time = '시간협의'
  else: 
    time = time.string 

  pay_h, pay_n = html[3].find_all("span")
  pay = f"{pay_h.string} {pay_n.string}"

  date = html[4].find("strong")
  if date is None:
    date = html[4].string
  else: 
    date = date.string 
  

  return {
    'place':place, 
    'title': title,
    'time':time,
    'pay':pay,
    'date':date
      }




def save_to_file(all_company_jobs):
  keys = all_company_jobs.keys()
  for a_key in keys:
    file_name = f"{a_key}.csv"
    file = open(file_name, mode ="w")
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])
    for job in all_company_jobs[a_key]:
      writer.writerow(list(job.values()))





all_company_jobs = {}
result = requests.get(alba_url)
soup = BeautifulSoup(result.text, "html.parser")
results = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li", {"class": "impact"})

for result in results:
  print("jobscrapping...")
  company_name = result.find("a",{"class":"goodsBox-info"}).find("span",{"class": "company"}).string
  company_url = result.find("a",{"class":"goodsBox-info"})["href"]
  all_company_jobs[company_name] = extract_job(company_url)
  
  

save_to_file(all_company_jobs)





    

