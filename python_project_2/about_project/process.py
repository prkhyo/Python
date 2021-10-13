


from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

# 서버 구축

app = Flask("SuperScrapper")


# route 밖에 선언되어 있기때문에 서버를 새로고침해도 초기화되지 않음 
# route 안에 있다면 report()가 실행될 때마다 초기화되어 db역할을 수행하지 못함
db = {}


# @ : decorater
# 바로 아래에 있는 함수만을 찾아 그 함수를 decorate하는 역할을 수행
# "/"로 접속 요청이 들어오면 home 함수 실행
@app.route("/")
def home():
  return render_template("home.html")


# dynamic urls
# 서로다은 url 들을 제어할 수 있음
# flask가 contact함수를 username 인자와 함께호출
# username은 함수 내에서 반드시 사용
@app.route("/<username>")  
def contact(username):
  return f"Hello your name is {username} !"


# query argument
# 사용자가 찾으려는 단어 가져오기
# /report?word=react
# word라는 이름으로 넘겨진 데이터 가져오기
# request.args -> dict 형태
# get을 통해 데이터를 가져올 수 있음
@app.route("/report")  
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:  
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    # 입력값word가 None일 경우 홈으로 redirect
    return redirect("/")


  # flask html 렌더링
  # render_template 인자를 통해 데이터를 template로 넘길 수 있음
  # html내 {{}}와 인자로 넘겨진 변수를 매핑하여 넣어줌
  return render_template("report.html", 
  searchingBy=word,
  resultsNumber = len(jobs) 
  )



# 리플릿에서 공개하는 웹 사이트 생성
# host="0.0.0.0" -> 리플릿에서 웹 결과창을 보기 위해 작성 
# local에서 작업한다면 host="0.0.0.0" 생략
app.run(host="0.0.0.0")



