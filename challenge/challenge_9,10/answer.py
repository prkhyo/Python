
1. reddit 사이트 스크래핑 하기 (scrapper.py)

- 헤더 설정하기 (Line 4) : Reddit 사이트는 웹 스크래핑을 차단하기 때문에 헤더를 포함하여야 합니다.
- aggregate_subreddits(subreddits) 함수 (Line 42 ~ 47)
- 이 함수는 main.py에서 사용자가 선택한 서브레딧 종류들을 받아와 각 서브레딧에 해당하는 데이터들을 
  scrape_subreddit(subreddit) 함수를 호출해 스크래핑 한 다음 모두 합산하여 aggregated 라는 변수에 담아
  리턴 시킵니다.
- scrape_subreddit(subreddit) 함수 (Line 25 ~ 40)
- 레딧 사이트에서 데이터를 긁어오는 함수입니다.
- 에러가 날 상황을 대비하여 try-except 문을 사용하였습니다.
- Line 29 ~ 30 : 데이터를 긁어 올 레딧 url을 가져온다음 requests 라이브러리에 headers를 추가해
  HTTP 요청을 보냅니다. 
  그 뒤 BeautifulSoup 라이브러리를 이용하여 레딧 홈페이지의 html 코드를 불러옵니다.
- Line 31 : 전체 정보를 담고 있는 div 태그의 클래스 명은 "rpBJOHq2PR60pnwJlUyP0" 이므로 .find() 를 
  사용하여 해당 영역만 뽑아와서 post_container 라는 변수에 저장합니다.
- Line 33 : post_container 에서 find_all() 를 사용하여 직계 자손들 중에서 div 태그의 클래스가 없는 것들만 
  모두 찾아 posts 리스트에 저장시켜줍니다.
  참고 문서 : recursive-argument
- Line 34 ~ 35 : posts 리스트를 차례로 돌면서 투표수(votes), 제목(title) 등 상세 정보를 추출해주는 
  extract_post 함수를 호출하여 exctracted_post 변수에 저장합니다.
- Line 36 ~ 40 : 만약 exctracted_post 가 존재한다면 all_posts 리스트에 삽입 시켜주고 이 리스트를 
  리턴시켜줍니다.
- extract_post(html, subreddit) 함수 (Line 7 ~ 23)
- 투표수(votes), 제목(title), 링크(link)를 추출해 주는 함수입니다.
- 홈페이지를 inspect 하여 정보가 들어있는 곳을 찾아낸 다음 추출하면 됩니다.
- Line 11 ~ 13 : Programming 사이트의 투표수를 보시면 "6.5k" 와 같이 뒤에 k가 붙어있습니다.
  투표수가 큰 순서대로 정렬시켜주기 위해 k는 숫자 1,000을 나타내므로 .replace() 을 사용하여 
  k를 없애준 다음 1,000을 곱해줍니다.
- 그런데 홈페이지를 잘 보면 "PROMETED"라는 광고가 중간에 끼워져 있습니다.
- 굳이 광고를 가져와서 홈페이지에 뿌려줄 필요가 없으므로 이 정보는 가져오면 안 됩니다.
- PROMETED의 코드를 잘 보시면 투표수(votes)와 제목(title)은 다른 데이터들과 똑같은 클래스 명에 저장되어 
  있는데 링크(link)를 담고 있는 a 태그가 다른 데이터들과는 달리 클래스 값을 가지고 있지 않습니다.
- 그러면 Line17 에서 PROMETED만 아무런 값을 가져오지 못하게 됩니다.
- 따라서 Line20 에서 if votes and title and link: 조건문을 사용하여 모든 값이 존재할 때만 추출한 값들을 
  리턴 시켜주면 PROMETED만 빼고 데이터를 보낼 수 있습니다.




2. main.py Line 6 ~ 20, home.html

- main.py의 subreddits 리스트에는 사용자가 선택할 요소들이 저장되어 있습니다.
- Line 18 ~ Line 20 : "/" 페이지에는 사용자가 원하는 것들을 선택할 수 있게 체크박스를 만들어줘야 합니다.
  그러기 위해서 "home.html" 에 subreddits 리스트를 전달해줍니다.
- home.html
- <form> 태그 안에 <input> 태그를 사용하여 subreddits 목록을 체크 박스로 만들어줍니다.
- Line 17 번째를 보시면 <form action="/read"> 라고 적혀있으므로 체크한 선택지만 "/read" 페이지로 넘어갑니다.





3. main.py Line 23 ~ 31 , read.html

- 사용자가 선택한 정보들만 레딧 사이트에서 추출하여 read.html에 뿌려줍니다.
- Line 26 ~ 28 : request.args 를 사용하여 home.html 페이지에서 받은 사용자의 선택지만 
  selected 리스트에 저장합니다.
- 그리고 scrapper.py의 aggregate_subreddits 함수로 selected 값을 보내 해당하는 데이터들을 넘겨받아 
  posts 에 저장합니다.
- 모든 데이터들을 투표수(votes)가 높은 순으로 정렬해야 하므로 .sort() 를 키 함수와 같이 사용합니다. 
  참고 문서 : 키 함수
- Line 31 : read.html로 selected와 postes에 저장된 정보를 보내 웹 사이트에 해당 정보들이 잘 보이도록 
  코딩해 주면 됩니다.




4. 결론

- 그동안 클래스명이 직관적인 홈페이지만 스크래핑 했었는데 이번 레딧 사이트는 클래스명이 난해하였지만 
  규칙이 존재하여 똑같은 방법으로 스크래핑 할 수 있었습니다.
- 또한 레딧 사이트는 스크래핑을 막고 있어서 헤더 값을 추가해 줘야 됐습니다.
- <form> 태그의 액션을 이용하여 다른 페이지로 값을 전달 후 지난 챌린지에 등장한 
  request.args 로 선택된 값만 데이터를 가져올 수 있었습니다.


