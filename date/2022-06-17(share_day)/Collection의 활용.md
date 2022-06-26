# Collection의 활용

#### 개요

- 코드에서 비교 연산 후 결정 되는 동작이 동일한 패턴으로 반복 된다면, Collection을 이용하여 가독성과 성능을 개선 할 수 있습니다.



#### Collection이란?

- 자료구조라고 할 수 있다 Array, List, Dictionary 등등의 데이터를 그룹으로 저장할 수 있는 메모리 구조를 말합니다.



#### 예시

```python
def forward():
    print('forward!')
    
def left():
    print('left!')
    
def right():
    print('right!')
    
def backward():
    print('backward!')
    
def moveA(key):
    if(key == 'w'):
        forward()
    elif(key == 'a'):
        left()
    elif(key == 'd'):
        right()
    elif(key == 's'):
        backward()
```

위와 같은 if-elif문을

```python
def forward():
    print('forward!')
    
def left():
    print('left!')
    
def right():
    print('right!')
    
def backward():
    print('backward!')
    
def moveB(key):
    dict = {'w': forward, 'a': left, 'd': right, 's':backward}
    
    func = dict.get(key)
    
    if func is not None:
        func()
```

Dictionary를 이용하여 가독성이 더 좋도록 바꿀 수 있습니다.



#### 장단점

Collection을 사용하고 안하고 모두 장단점이 있기 때문에, 메모리 사용량, 함수 실행 속도, CPU 연산량 등 다각도에서 고려해야합니다.



#### 기본 과제

```javascript
const date = new Date()
const year = date.getFullYear()  // 년도
const month = date.getMonth()  // 달

var days = null

switch(month){
        
    case 0:
    case 2:
    case 4:
    case 6:
    case 7:
    case 9:
    case 11:
        days = 31;
        break;
        
    case 3:
    case 5:
    case 8:
    case 10:
        days = 30;
        break;
    case 1:  // 윤년에 따라 달라지는 날수
        if ((year%4 == 0) && (year % 100 !=0) || year % 400 == 0)
            days = 29;
        else
            days = 28;
        break
}

console.log(days + ' days for ' + year + '-' + (month + 1))  //해당 달의 날 수 출력
```

해당 코드는 javaScript로 짜여있는데, python이 좀 더 다루기 쉬우므로 python으로 해결했습니다.



1. List in 연산자를 사용

```python
# list사용
# in 연산자를 사용
from datetime import date, datetime
today = date.today()  # 오늘 년 월 일
year = today.year  # 오늘 년
month = today.month  # 오늘 월
d = today.day  # 일단 일도 저장

def by_list(month):
  li1 = [1, 3, 5, 7, 8, 10, 12]  # 31일이 되는 달 저장
  li2 = [4, 6, 9, 11]  # 30일이 되는 달 저장
  if month in arr1:
    days = 31
  elif month in arr2:
    days = 30
  else:  # 2월이라면 윤년을 고려해야 하므로,,
    if (year%4 == 0 and year % 100 !=0) or year % 400 == 0:
      days = 29
    else:
      days = 28
  print(str(days) + ' days for ' + str(year) + '-' + str(month))
by_list(month)

'''
output
$ python collection.py
31 days for 2022-6
'''

```



2. List index 사용

```python
# list 사용 2
# index로 접근
from datetime import date, datetime
today = date.today()
year = today.year
month = today.month
d = today.day

def by_dictionary(month):
  li = [31, 29 if (year%4 == 0 and year % 100 !=0) or year % 400 == 0 else 28, 
  31, 30, 31, 30, 
  31, 31, 30, 31,
  30, 31
  ]  # 하나의 dictionary생성
  print(str(li[month-1]) + ' days for ' + str(year) + '-' + str(month))
by_dictionary(month)
```



3. dictionary 사용

```python
#dictionary 사용

from datetime import date, datetime
today = date.today()
year = today.year
month = today.month
d = today.day

def by_dictionary(month):
  dic = {1: 31, 2: 29 if (year%4 == 0 and year % 100 !=0) or year % 400 == 0 else 28, 
  3: 31, 4: 30, 5: 31, 6: 30, 
  7: 31, 8: 31, 9: 30, 10: 31,
  11: 30, 12: 31
  }  # 하나의 dictionary생성
  print(str(dic.get(month)) + ' days for ' + str(year) + '-' + str(month))
by_dictionary(month)

'''
output
$ python dic.py
30 days for 2022-6

input2
by_dictionary(2)
output2
$ python dic.py
28 days for 2022-2
'''
```



#### 심화 과제

간단한 예제를 생각했습니다. 3개의 입력을 갖는 OR 연산을 구현해보고자 했습니다.

```python
def non_collection(a, b, c):
    if a == 1 and b == 1 and c == 1:
        ans = 1
    elif a == 1 and b == 1 and c == 0:
        ans = 1   
    elif a == 1 and b == 0 and c == 1:
        ans = 1
    elif a == 0 and b == 1 and c == 1:
        ans = 1   
    elif a == 1 and b == 0 and c == 0:
        ans = 1
    elif a == 0 and b == 1 and c == 0:
        ans = 1   
    elif a == 0 and b == 0 and c == 1:
        ans = 1
    elif a == 0 and b == 0 and c == 0:
        ans = 0
    print(f'non_collection: {ans}')


def collection(a, b, c):
    tmp = str(a) + str(b) + str(c)
    dic = {
        '111': 1,
        '110': 1,
        '101': 1,
        '011': 1,
        '100': 1,
        '010': 1,
        '001': 1,
        '000': 0,
    }
    ans = dic.get(tmp)
    print(f'collecction: {ans}')


def logic(a, b, c):
    ans = a or b or c
    print(f'logic: {ans}')


# 출력 비교 구문
for p in range(8):
    num = bin(p)[2:]
    num = num.zfill(3)
    print(f'# {num}')
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    non_collection(a, b, c)
    collection(a, b, c)
    logic(a, b, c)
    
'''
# 000
non_collection: 1
collecction: 0
logic: 0
# 001
non_collection: 1
collecction: 1
logic: 1
# 010
non_collection: 1
collecction: 1
logic: 1
# 011
non_collection: 1
collecction: 1
logic: 1
# 100
non_collection: 1
collecction: 1
logic: 1
# 101
non_collection: 1
collecction: 1
logic: 1
# 110
non_collection: 1
collecction: 1
logic: 1
# 111
non_collection: 1
collecction: 1
logic: 1
'''

```

세 가지 방법으로 구현 하였습니다.

위와 같이 간단한 로직으로 구현되는 경우는, collection을 쓰지 않는 것이 가독성이 더 뛰어나다는 것을 알 수 있습니다.
