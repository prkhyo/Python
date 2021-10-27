

# Challenge goals:
# 보일러플레이트를 이용하여 세 종류의 웹사이트에서 정보를 긁어와 원격 직업을 찾는 
# "job scrapper"를 만드세요.


####### 조건 #######
# 웹사이트는 .csv 파일 내보내기가 가능해야 됩니다.
# 반복 검색 속도가 빨라지기 위해서 fakeDB를 구현해야 됩니다.
# 아래에 있는 세 종류의 웹사이트를 모두 스크랩해야 됩니다.
# https://weworkremotely.com/
# https://stackoverflow.com/jobs
# https://remoteok.io/
# 세 사이트나 스크래핑 해야 하므로 코드를 관리하기 위해 사이트마다 스크래핑 해오는 코드를 
# 따로따로 만들어 관리하는 걸 추천합니다.



"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
from ro import get_jobs as get_ro_jobs
from so import get_jobs as get_so_jobs
from wwm import get_jobs as get_wwm_jobs
from exporter import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
  return render_template("home.html")



@app.route("/report")  
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:  
      jobs = get_ro_jobs(word) + get_so_jobs(word) + get_wwm_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", 
  searchingBy=word,
  resultsNumber = len(jobs),
  jobs = jobs 
  )


@app.route("/export")
def export(): 
  try:
    word = request.args.get('word')
    if not word:
      raise Exception() 
    word = word.lower()
    jobs = db.get(word) 
    if not jobs: 
      raise Exception()
    save_to_file(jobs) 
    return send_file("jobs.csv")
  except:
    return redirect("/")
  
    


app.run(host="0.0.0.0")



