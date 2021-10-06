


# 1. variable type

a_string = "like this"
a_number = 3
a_float = 3.12
a_none = None   # 존재하지 않는다, 없다
a_boolean = False

super_long_variable = True # 파이썬의 변수명 표기법 (snake case)




# 2. sequence type

# list
# 인덱스 O, 변경 가능, 하나의 list에 다양한 타입 가능

days_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_list[0])        # Mon
print("Mon" in days_list)  # True
print(len(days_list))      # 5

days_list.append("Sat")    
print(days_list)          # ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

days_list.reverse()
print(days_list)          # ['Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon']

somethig = ["string", 7, True, None, 5.34]
print(somethig)           # ['string', 7, True, None, 5.34]



# tuple
# 인덱스 O, 변경 불가능

days_tuple =  ("Mon", "Tue", "Wed", "Thur", "Fri")



# dictionary 
# 변경 가능

hyo = {
  "name" : "hyo",
  "age" : 26,
  "korean" : True
}

print(hyo)       # {'name': 'hyo', 'age': 26, 'korean': True}
print(hyo["age"])  # 26

hyo["handsome"] = True  # 값 append
print(hyo)       # {'name': 'hyo', 'age': 26, 'korean': True, 'handsome': True}




# 3.function

# 내장 함수

# print() : 출력 함수

# len(): 입력값의 길이(요소의 전체 개수)를 돌려주는 함수 

# int(), bool(), str(), float() : 타입 변경

# abs(): 절댓값을 돌려주는 함수

# all(): 반복 가능한(iterable) 자료형을 입력인수로 넣고, 모두 참이면 True, 하나라도 거짓이면 False를 돌려주는 함수
#        반복 가능한 자료형 -> 리스트, 튜플, 문자열, 딕셔너리, 집합 등

# any(): 반복 가능한(iterable) 자료형을 입력인수로 넣고, 하나라도 참이 있으면 True, 모두 거짓일 경우에만 False를 돌려주는 함수
#        반복 가능한 자료형 -> 리스트, 튜플, 문자열, 딕셔너리, 집합 등

# chr(): 아스키(ASCII) 코드값을 입력받아, 그 코드에 해당하는 문자를 출력하는 함수

# enumerate(): 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 돌려주는 함수

# eval(): 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수

# filter(): 첫 번째 인수로 함수이름, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받아
#           그 함수에 차례로 대입하면서 입력되었을때 참인 것만 묶어서 돌려주는 함수
        

# input(): 사용자 입력을 받는 함수

# list(): 반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수

# tuple(): 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수

# map(): 함수(f)와 반복 가능한(iterable) 자료형을 입력받아, 입력된 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 돌려주는 함수
     

# max(): 반복 가능한(iterable) 자료형을 입력받아 최대값을 돌려주는 함수

# min(): 반복 가능한(iterable) 자료형을 입력받아 최솟값을 돌려주는 함수

# pow(x,y): x의 y제곱한 결과값을 돌려주는 함수

# sorted(): 반복 가능한 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수

# type(): 입력값의 자료형이 무엇인지 알려주는 함수

# zip(iterable*): 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
# ex) print(list(zip("abc","def"))) -> [('a', 'd'), ('b', 'e'), ('c', 'f')]




# 사용자 정의 함수

def say_hello():  # say_hello 함수 작성 
  print("hello")  


say_hello()       # say_hello 함수 실행



def say_bye(who): 
  print("bye", who)  


say_bye("hyojin")    # bye hyojin


def plus(a, b):
  print(a + b)

plus(4, 5)  # 4 + 5 = 9


def minus(a, b = 0): # 인자에서 변수 선언과 동시에 값 지정 가능 
  print(a - b)

minus(8)   # 8 - 0 = 8



def p_plus(a, b):
  print(a + b)   # 값을 콘솔로 출력 

def r_plus(a, b):
  return a + b   # 값을 함수 외부(호출부)로 return
                 # return과 동시에 함수 종료

p_result = p_plus(2, 3)  # 단순히 해당 function 호출 (return X)
r_result = r_plus(2, 3)  # 해당 function은 return된 값으로 치환됨

print(p_result, r_result)   # None 5




# keyword argument
# 인자인데 위치에 따라서 정해지는게 아닌 argument의 이름으로 쌍을 이뤄주는 것
# argument가 여러개인 경우 유용하게 사용할 수 있음

def score(kor, eng):
  print(kor, eng)  # 100, 90

score(eng = 90, kor = 100) # 이 경우, 인자의 순서를 신경 쓸 필요 X 
                           # 인자의 이름만 신경쓰면 됨




# string 안에 변수 포함하여 작성하는 법
# f(format)를 string 앞에 쓰고, 변수의 이름을{ }로 감싸줌

def say_hi(name, age):
  return f"Hello {name} you are {age} years old"

hi = say_hi("hyojin", 26)
print(hi)   # Hello hyojin you are 26 years old





# 4. Conditionals
# 조건문
# 기본적으로 소프트웨어의 로직을 컨트롤할 때 사용


def plus(a, b):
    if type(b) is int or type(b) is float:
      return a + b
    else:
      return None 


def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18:
    print("you are new to this!") 
  elif age > 20 and age < 25:
    print("you are still kind of young")  
  else:
    print("enjoy your drink")  


age_check(23)




# 5. loop
# 반복문

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

for day in days:
  if day is "Wed":
    break    # for문의 loop를 break
  else:  
    print(day)



