

# Web Scrapping project using Python/Flask

자바 기반 웹 프레임워크로는 대표적으로 Spring이 있듯이, <br> 파이썬 기반 웹 프레임 워크로는 대표적으로 Flask, Django가 있다.

<br> 

### Flask vs Django


**FLASK**는 파이썬을 기반으로 한 마이크로 웹 프레임워크로,<br> 
 매우 심플하고 가볍지만 핵심적인 내용과 기능을 가지고 있어 간단한 웹 사이트, <br> 
 혹은 간단한 API 서버를 만드는 데에 특화 되어있다. <br> 
또한 기능들을 확장 모듈들을 통해 지원하고 있고, 최소한의 규칙만 존재하기 때문에 자유도가 높다.


**Django**는 파이썬을 기반으로 한 풀 웹 프레임워크로, 모든 기능을 지원하는 프레임워크다.<br> 
매우 많은 기능들을 자체적으로 가지고 있고, 개발자는 그 규칙에 맞추어 코딩하여야 한다.


→  Flask 는 소규모의 어플리케이션을 빠르게 만들 수 있고, 배포 환경에 따라 대규모 어플리케이션의 기능 확장의 역할을 하기 쉬운 장점이, Django는 대규모의 어플리케이션을 빠르게 만들 수 있으며, 기본으로 제공 해 주는 기능이 많은 장점이 있다. 

→ 이번 프로젝트에서는 가볍게 배울 수 있고, 가볍게 사용 할 수 있으며, 가볍게 배포 할 수 있는 Flask를 사용하여 프로젝트 1에서 진행했던 scrapper를 확장하여  입력받은 언어에 대한 job 정보를 scrapping 하여 브라우저로 그 결과를 보여주는 간단한 웹 서비스를 구현해볼 것이다.



***


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

* csv
```
- python으로 csv 파일을 쓸 때 사용
- writer함수 이용
```

<br>

* flask
```
- 모두가 접근할 수 있는 간단한 웹 사이트를 만들기위해 사용
- render_template / request / redirect / send_file 이용
```


<br>
<br>

### project plan

1. 웹사이트와 폼 생성 (home.html, roport.html)
2. python을 사용하여 stackoverflow, indeed 각 사이트에 대해 검색 키워드와 일치하는 <br>
   job정보를 스크래핑하는 scrapper 생성(총 2개의 scrapper)
3. 해당 입력폼에 사용자가 python, go, java 등의 키워드를 입력하고 search 버튼을 누르면 <br>
   키워드를 가지고 두 개의 사이트에 대한 각각의 scrapper가 동작 <br>
(두 개의 작동 결과를 합쳐서 하나의 결과로 값을 반환해줄 것)
4. 반환 값을 전달 받아 웹 사이트에 바로 결과를 띄워줄 것(결과를 표로 보여줄 것)<br>

5. 다운로드 버튼도 제공하여 만약 사용자가 다운로드를 원한다면 해당 데이터를 <br>csv파일로 다운로드할 수 있도록 구현


<br>











