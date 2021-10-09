


# plan

# indeed에서 정보를 가져옴
# 그 다음 stackoverflow에서 정보를 가져옴 (두 사이트를 왔다갔다 하지 않을 것)
# 두 사이트에서 가져온 모든 결과를 엑셀시트에서 보여줄 것


# 각 사이트에서 정보를 가져오기 위해 해야할 일 순서 !
# 첫째, 마지막 페이지 정보 가져오기
# 둘째, 가져온 마지막 페이지 정보를 이용하여 페이지 수 만큼 requests 생산
# 셋째, 첫 페이지 부터 마지막 페이지까지 job 추출






# 1. 스크랩핑할 url (페이지 정보 반영)
# [indeed]         https://www.indeed.com/jobs?q=python&limit=50
# [stackoverflow]  https://stackoverflow.com/jobs?q=python





# 2. python을 사용하여 스크랩핑할 url로 접근, 해당 URL에서 자료(html) 추출
# 파이썬에서 요청을 만드는 기능을 모아 놓은 requests 패키지를 설치하여 사용

# [indeed] 

import requests

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

indeed_result = requests.get(URL)


# [stackoverflow]





# 3. HTML에서 페이지 정보 추출
# 방대한 html정보에서 필요로 하는 데이터(직업 데이터, 총 데이터 수량, 페이지 정보 등등)를 효율적으로 뽑아내기 위해 BeautifulSoup4 온라인 라이브러리 사용
  
# [indeed] 

from bs4 import BeautifulSoup

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") # Soup을 사용하여 데이터 파싱


# 페이지 정보 추출

pagination = indeed_soup.find("div", {"class": "pagination"})


# find_all : 찾은 결과를 리스트로 저장
links = pagination.find_all('a')

pages = []

for link in links[:-1]: # 마지막 데이터는 제외
  # pages.append(int(link.find("span").string)) 아래 코드와 동일한 결과 
  # → 굳이 a 태그 내부에 있는 span 태그를 찾아 string을 가지고 오지 않아도 a태그 내부에 string이 오직 하나있다면 
  #   Soup이 알아서 a태그 내부에 있는 해당 string을 찾아 가지고 옴
  pages.append(int(link.string))
  
max_page = pages[-1] # 마지막 페이지 정보


# [stackoverflow]






# 4. 최대 페이지 수만큼 각 페이지에 해당하는 request 요청을 생산

# [indeed] 

# 한 페이지 당 50개의 job데이터 출력
# start=0   -> 1 페이지
# start=50  -> 2 페이지
# start=100 -> 3 페이지
# start=150 -> 4 페이지
# start=200 -> 5 페이지
# URL에 추가해 줄 것

for page in range(max_page): # 0 ~ 마지막페이지 - 1(0은 1페이지를 지칭)                    
  print(f"start={page*50}")
  result = requests.get(f"{URL}&start={page*LIMIT}")
  

# [stackoverflow]






# 5. request 요청에 따라 각 페이지로 이동 후 일자리 정보를 추출해서 변수에 담기 -> 모든 일자리 반환해 줄 것
  
# [indeed] 

def extract_job(html):
  # job data에서 class 명이 jobTitle인 h2를 찾고, 그 안에 title이 존재하는 span을 찾아서 태그 내부의 string을 가져옴
  # title: 직무 title
  title = html.find("h2",{"class" : "jobTitle"}).find("span", title = True).string

  # company: 회사명
  company = html.find("span",{"class":"companyName"})
  if company: # company가 존재하는 경우
    company_anchor = company.find("a")
    # span 내부에 a태그가 있는 경우 a태그에 있는 string을 가져오고,
    # a태그가 없는 경우, 해당 span 태그에 있는 string을 가져옴
    if company_anchor is not None:
      company = company_anchor.string
    else:  
      company = company.string
    company = company.strip()  
  else:
    company = None

  # location: 회사 위치
  location = html.select_one("pre > div").text

  # job_id: 각 job에 대한 지원링크 생성시 사용
  job_id = html['data-jk']
  

  return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}




def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page + 1}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser") 
    # results : job list
    results = soup.find_all("a", {"class": "fs-unmask"})
    for result in results:
      # result: a job data
      job = extract_job(result)
      jobs.append(job)
  return jobs 



# [stackoverflow]






# 6. 호출 함수 작성


# [indeed] 

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs









