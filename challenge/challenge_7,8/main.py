


# Challenge goals:
# Using this boilerplate we are going to build a mini clone of the Hacker News Website 
# using the Hacker News Search API and Flask.
# 해커뉴스 API와 Flask를 활용하여 해커뉴스 웹사이트 클론코딩을 진행합니다.
# 위의 힌트 (Clues)를 활용하여, 필요조건 (Requirements) 에 맞추어 과제를 완수하세요.
# https://news.ycombinator.com/
# https://hn.algolia.com/api
# https://uniformlinednature.serranoarevalo.repl.co/


# 클론코딩할 웹사이트는 다음과 같은 경로를 가집니다.
# /
# /?order_by=new
# /?order_by=popular
# /＜id＞


#### 조건 #####
# 강의 4.6와 같은 fakeDB를 구현하여 'new' 및 'popular'가 더 빠르게 로드 될 수 있도록합니다.
# 클론 웹사이트는 order_by의 현재 선택 사항을 반영해야 합니다.
# 메인 페이지 "/"는 기본적으로 order_by가 popular로 선택되어야 합니다.
# 각 타이틀에 링크를 걸어 그 타이틀에 해당하는 모든 코멘트들을 볼 수 있도록 합니다.



import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")




@app.route("/")
def home():
  order_by = request.args.get('order_by', 'popular')
  if order_by not in db:
    print("Requesting")
    if order_by == 'popular':
      news = requests.get(popular)
    elif order_by == 'new':
      news = requests.get(new)
    results = news.json()['hits']
    db[order_by] = results
  results = db[order_by]
  return render_template("index.html", order_by=order_by, results=results)


@app.route("/<id>")
def detail(id):
  detail_request = requests.get(make_detail_url(id))
  result = detail_request.json()
  return render_template("detail.html",result=result)

app.run(host="0.0.0.0")



