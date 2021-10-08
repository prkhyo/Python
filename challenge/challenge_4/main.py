

import os
import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number: ")

currency_codes = []

def extract_code():
  result = requests.get(url)
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
      cnt += 1
      nation={
        "name": imsi[0].capitalize(), 
        "code": imsi[2],
        "no": cnt 
      }
      currency_codes.append(nation)


def nation_info_output(codes):
  for code in codes:
    print(f"# {code['no']} {code['name']}")
  


extract_code()
nation_info_output(currency_codes)


while True:
  try:
    number = int(input("#: "))
    if number >= 1 and number <= len(currency_codes):
      for code in currency_codes:
        if code['no'] == number:
          print(f"You chose {code['name']}") 
          print(f"The currency code is {code['code']}")
          break
        else:
          continue  
      break     
    else:
      print("Choose a number from the list.") 
    
  except ValueError:
    print("That wasn't a number...")

os.system("clear")




