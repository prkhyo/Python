


# plan

# indeed에서 정보를 가져윰
# 그 다음 stackoverflow에서 정보를 가져옴 (두 사이트를 왔다갔다 하지 않을 것)
# 두 사이트에서 가져온 모든 결과를 엑셀시트에서 보여줄 것





# 1. 스크랩핑할 url (페이지 정보 반영)
# [indeed]         https://www.indeed.com/jobs?q=python&limit=50
# [stackoverflow]  https://stackoverflow.com/jobs?q=python



# 2. python을 사용하여 스크랩핑할 url로 접근, 해당 URL에서 자료(html) 추출
# 파이썬에서 요청을 만드는 기능을 모아 놓은 requests 패키지를 설치하여 사용


import requests

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_result.text)



# 3. HTML에서 정보 추출
# 방대한 html정보에서 필요로 하는 데이터(직업 데이터, 총 데이터 수량, 페이지 정보 등등)를 효율적으로 뽑아내기 위해 BeautifulSoup4 온라인 라이브러리 사용
  
