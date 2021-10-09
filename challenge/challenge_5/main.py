

# <Challenge goals> 
# Challenge4에서 완성한 코드에 다음 작업을 수행할 수 있도록 기능을 확장하세요.
#  1. 국가와 통화 코드 목록이 출력된 후 사용자는 두 개의 국가를 선택할 수 있습니다.
#  2. 그리고나서 사용자는 국가 a와 국가b 사이에서 환전하고자 하는 금액을 입력합니다.
#  3. 두 나라의 통화 코드와 환전하려는 금액을 다음과 같은 URL로 보냅니다.
#  4. beautifulSoup 라이브러리를 사용하여 Transfer Wise 사이트에서 정보를 긁어와 환전 결과를 얻습니다.




import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""



currency_url = "https://www.iban.com/currency-codes"
convert_url = "https://wise.com/gb/currency-converter/"


currency_codes = []
first_nation = {}
second_nation = {}


def extract_code():
  result = requests.get(currency_url)
  soup = BeautifulSoup(result.text, "html.parser") 
  table = soup.find("table", {"class": "table"})
  trs = table.find_all("tr")
  cnt = 0

  for tr in trs[1:len(trs)]:
    tds = tr.find_all("td")
    imsi = []
    for td in tds:
      imsi.append(td.text)
    if imsi[1] == 'No universal currency':
      continue
    else:
      nation={
        "name": imsi[0].capitalize(), 
        "code": imsi[2],
        "no": cnt 
      }
      currency_codes.append(nation)
      cnt += 1


def nation_info_output(codes):
  for code in codes:
    print(f"# {code['no']} {code['name']}")
  

def search_nation(num):
  for code in currency_codes:
    if code['no'] == num: 
      return code
      

def chooseNation():
  global first_nation
  global second_nation
  print("Where are you from? Choose a country by number.")
  print()
  first_nation_num = int(input("#: "))
  first_nation = search_nation(first_nation_num)
  print(first_nation['name'])
  print()
  print("Now choose another country.")
  print()
  second_nation_num = int(input("#: "))
  second_nation = search_nation(second_nation_num)
  print(second_nation['name'])


  

print("Welcome to CurrencyConvert PRO 2021")
print()
extract_code()
nation_info_output(currency_codes)
print()
chooseNation()
print()



def convert(amount):
  global first_nation
  global second_nation
  url = f"{convert_url}{first_nation['code']}-to-{second_nation['code']}-rate"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser") 
  rate = soup.find("span", {"class": "text-success"}).string
  convert_result = float(rate) * amount

  amount_formating = format_currency(amount, first_nation['code'], locale="ko_KR")
  result_formating = format_currency(convert_result, second_nation['code'], locale="ko_KR")

  print(f"{amount_formating} is {result_formating}")
  
  
 

while True:
  print(f"How many {first_nation['code']} do you want to convert to {second_nation['code']}?")
  try:
    amount = int(input())
    convert(amount)
    break
  except ValueError:
    print("That wasn't a number...")
    print()





