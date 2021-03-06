

# Web Scrapping project using Python


### What is Web Scrapping?

Web Scrapping 이란 **웹 상의 데이터를 추출하는 것**<br>
즉, 웹 사이트에서 **원하는 데이터를 추출**하여
추출한 데이터를 **원하는 형식으로 가공하는 것**을 말함

***
<br>

## Web Scrapping의 3가지 단계

* **Scraping** : 데이터 가져오기 
* **Parsing** : 데이터 파싱
* **Manipulation** : 데이터 가공

<br>

## About this project

### IDE
* repl.it (https://repl.it/)

### skills

* Requests <br>
(https://requests.readthedocs.io/projects/3/)
(https://github.com/psf/requests)
```
- python으로 URL에서 자료 추출하기위해 사용
- python 기본 라이브러리 urllib을 이용해도 충분히 html을 scrapping 할 수 있지만, 
  requests라는 더 강력한 기능을 가진 온라인 라이브러리를 이용해서 좀 더 편리하게 scrapping
```

<br>

* Beautiful Soup4<br>
(https://www.crummy.com/software/BeautifulSoup/)

```
- HTML에서 정보를 추출하기위해 사용
```

<br>

### project plan

1. 유명한 구직 사이트 indeed, stackoverflow에서 파이썬 관련 일자리를 찾는 상황이라고 가정<br>
2. 각 사이트 검색창에 'python'이라는 키워드로 검색하게되면 새로운 url로 들어가면서 다양한 검색 결과를 볼 수 있음<br>
3. **python을 사용하여 scrapper 생성**<br>
4. 만들어진 scrapper가 **각 사이트에 등록된 일자리를 전부 가져옴** <br>
5. indeed 와 stackoverflow 에서 **가져 온 모든 일자리 정보를 엑셀시트에 옮김**
(엑셀 시트 한 줄 당 하나의 job 정보 표시)


<br>












