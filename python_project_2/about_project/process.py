


# plan

# 개발한 scrapper를 웹서버에 넣는 작업
# 모두가 접근할 수 있는 웹 사이트 만들기
# 사용자가 python, go, java 등의 키워드를 입력하면 그 언어에 해당하는 직업들을 보여줌
# 즉, 파이썬뿐 아니라 입력받은 언어에 대한 job 정보를 scrapping 하는 scrapper를 만들 것.

# 웹사이트와 폼을 만들어서 searchbox에 직업 종류를 입력하고 search 버튼을 누르면 csv파일을 만드는 대신 
# 웹 사이트에 바로 결과를 띄워줄 것(결과를 표로 보여줄 것)
# 만약 사용자가 다운로드를 원한다면 다운로드할 수 있도록 다운로드 버튼도 제공


# 웹 확장을 위해 Flask 사용

# Flask ?
# 파이썬으로 웹사이트를 만들 수 있게 해주는 micro-framework
# 수많은 설정을 다 세팅해줄 필요가 없음






# 1. flask 설치




# 2. 만들었던 scrapper 수정
# 어떤 입력을 해도 찾을 수 있도록




# 3. dict 자료형을 이용한 fake DB 생성
# 매 번 스크래핑되는 것을 기다려야하는 문제 해결
# db에 react를 검색한 결과가 들어있다면 다시 재검색했을 때 scrapper 동작 없이 저장되어있던 결과를 보여줌 




# 4. 검색 폼 작성
# 검색 키워드 입력 후 버튼 클릭시 '/report'로 이동 
# (url로 이동할 때 word라는 인자name으로 입력 값이 함께 넘어감)




# 5. 검색 결과를 html페이지로 출력

@app.route("/report")  
def report():
  # request 함수 이용해서 인자의 이름이 word와 같은 값을 가져옴
  # 이때, word가 None일 경우(검색어를 입력하지 않은 경우), home으로 이동
  # word가 존재할 경우, 소문자 처리
  word = request.args.get('word')
  if word:
    word = word.lower()
    # fake DB에  word와 일치하는 키값이 존재할 경우 (검색기록이 남아있는 경우)
    # 해당 key로 저장된 values 데이터를 가져와 jobs라는 변수에 저장
    # fake DB에  word와 일치하는 키값이 존재하지 않는 경우,
    # scrapper 작동 후 결과값인 job데이터들을 word라는 key값으로 fake DB에 추가    
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:  
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  # render_template 함수를 리턴하면서 report.html를 렌더
  # 이때, 렌더링시 필요한 데이터 word와 jobs를 함께 넘김
  # 넘길 변수이름 지정-> 렌더링할때 지정해준 이름과 매핑되는 변수에 데이터가 들어가게 됨
  return render_template("report.html", 
  searchingBy=word,
  resultsNumber = len(jobs),
  jobs = jobs 
  )





# 5-1. 렌더링
# html에서는 
# 파이썬 변수를 보여주기 위한 코드 ->  {{ }} 
# 파이썬 코드를 실행하기 위한 코드 ->  {% %} 
# 두 가지를 사용하여 넘겨받은 데이터를 매핑되는 변수에 넣어줌





# 6. 파일로 저장 후 내려받기
# export버튼 클릭시 해당 url로 이동 
# (url로 이동할 때 word라는 인자name으로 검색키워드값이 함께 넘어감)


@app.route("/export")
def export():
  # try에 작성한 코드를 실행하다가 try블록 안 어디서든 Exception이raise되면 except 내부에 작성한 코드가 실행됨 
  try:
    # request 함수 이용해서 인자의 이름이 word와 같은 값을 가져옴
    # 이때 word가 None일 경우 예외 발생 ->  home으로 이동
    # word가 존재할 경우, 소문자 처리 후 word라는 이름의 key로 저장된 values 데이터를 가져와 jobs라는 변수에 저장
    word = request.args.get('word')
    if not word:
      raise Exception() # 예외를 발생시킴
    word = word.lower()
    jobs = db.get(word) 
    # fake DB에  word와 일치하는 키값이 존재하지 않는 경우, 예외 발생 ->  home으로 이동
    # fake DB에  word와 일치하는 키값이 존재할 경우 해당 jobs데이터를 csv 파일로 생성하는 save_to_file 함수 실행
    if not jobs: 
      raise Exception()
    save_to_file(jobs) 
    return send_file("jobs.csv") # 생성할 파일명을 인자로 가지는 send_file 함수를 리턴하면서 사용자에게 넘겨줌
  except:
    return redirect("/")








