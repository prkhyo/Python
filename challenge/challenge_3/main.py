


import requests


def add_url():

  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  URLS = list(input().split(','))
  
  for a_url in URLS:
    a_url = a_url.strip()
    if '.' not in a_url:
      print(f"{a_url} is not a valid URL.")  
      break
    if "//" not in a_url:
      a_url = "http://" + a_url 
      
    url_check(a_url)

  over_check()




def url_check(a_url):
 
  try:
    result = requests.get(a_url)
    if result.status_code == 200:
      print(f"{a_url} is up!")
    else:
      print(f"{a_url} is down!") 
  except:
    print(f"{a_url} is down!")

   

def over_check():
  print("Do you want to start over? y/n ", end='')
  answer = input().strip()

  if answer != 'y' and answer != 'n':
    print("That's not a valid answer")
    over_check()
  elif answer == 'y':
    add_url()
  elif answer == 'n':
    print("bye!")  



add_url()





