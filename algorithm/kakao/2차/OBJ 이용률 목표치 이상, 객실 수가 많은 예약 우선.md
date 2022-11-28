OBJ: 이용률 목표치 이상, 객실 수가 많은 예약 우선





#### 변수

호텔

- W : 한 층의 객실 수
- H : 층 개수



객실

- ABBB or AABBB : A는 층 B는 위치



체크 아웃은 1100, 체크인은 1400



예약 요청

- id : 6자리 정수
- 객실 수
- 체크인 날짜 : 예약 요청 이후 1~21 뒤
- 체크 아웃 날짜



예약 관리

- 답변 기한 : min(예약 요청이 들어온 날짜 +14, 체크인 날짜-1)



객실 배정

- 배정은 같은 층에서 인접한 연속된 객실



#### 시나리오1

W=20, H=3

totalDate = 1~200

avgReservation = 1

reserveRoom = 1~10

reserveDate = 1~20 

obj = 60%



```python
# 문제 시작
start_res = parser.post('/start', headers=post_headers, data=json.dumps({'problem': 1}))
print(f'start_res : {start_res}')

# 문제 설정
auth_key = start_res['auth_key']
headers = {
    'Authorization': auth_key,
    'Content-Type': parser.content_type,
}

# NewRequests API (id, 객실 수, 체크인 날짜, 체크 아웃 날짜)
newRequest_res = parser.get('/new_requests', headers=headers)
print(newRequest_res)

# Reply API (현재 날짜)
reply_res = parser.put('/reply', headers=headers, data=json.dumps({'id': 1, 'reply':'accepted'}))

# Simulate API( )
simulate_res = parser.put('/simulate', headers=header, data=json.dumps({'id':1, 'reply':1001}))

#Score API(점수)(정확성, 효율성, 페널티, 총점)
score_res = parser.get('/score', headers=header)

```





1. 문제 풀이 방안

- 먼저 대기열을 생성 [(id, 객실수, 체크인 날짜, 체크 아웃 날짜, 유통기한, 체류 기간)]
- 정렬 순서는 [(객실 수, 유통기한, 체크 인 날짜, 체류 기간, 체크 아웃 날짜, id)]



2. 매일 해당 순서로 확인 후 집어 넣자





3. 우선순위가 떨어지는 예약들은 일단 숙성
   - 객실수가  2이하, 일단 pass 하고 마지막 전날 확인
   - 객실수가 4이하 3일 이하 남으면 확인
   - 10 이상이면 바로 검토
   - 애매하면 점수를 매기자
     - 객실수 * 날짜 
   - 또 예외 처리 할 수 있는 것은 성수기





```python
# 제출용
# Python
import json
import requests
from collections import deque
from pprint import pprint 

class Parser(object):
    def __init__(self, token: str, base_url: str, verbose=0):
                
        if base_url[-1] == '/':
            base_url = base_url[:-1]
        self.base_url = base_url
        self.content_type = 'application/json'
        self.token = token
        self.verbose = verbose


    def post(self, x, headers=None, data=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.post(url, headers=headers, data=data)
        # if self.verbose:
        #     print(response.status_code)
        return response.json()
    
    def get(self, x, headers):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        # print(f'url : {url}, {headers}')
        response = requests.get(url, headers=headers )
        # if self.verbose:
        #     print(response.status_code)
        return response.json()
    
    def put(self, x, headers=None, data=None):
        if x[0] != '/':
            x = '/' + x
        url = self.base_url + x
        response = requests.put(url, headers=headers, data=data)
        # if self.verbose:
        #     print(response.status_code)
        return response.json()

token = '9c20db1e333feb596eeeee63b65df8bb'
base_url = f'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'

# parser = Parser(token=token, base_url=base_url, verbose=1)
# post_headers = {
#     'X-Auth-Token': parser.token,
#     'Content-Type': parser.content_type,
# }

# 문제 시작
# start_res = parser.post('/start', headers=post_headers, data=json.dumps({'problem': 1}))
# print(f'start_res : {start_res}')

# 문제 설정
# auth_key = start_res['auth_key']
# headers = {
#     'Authorization': auth_key,
#     'Content-Type': parser.content_type,
# }

# NewRequests API (id, 객실 수, 체크인 날짜, 체크 아웃 날짜)
# newRequest_res = parser.get('/new_requests', headers=headers)
# print(newRequest_res)

# Reply API (현재 날짜)
# reply_res = parser.put('/reply', headers=headers, data=json.dumps({'id': 1, 'reply':'accepted'}))

# Simulate API( )
# simulate_res = parser.put('/simulate', headers=header, data=json.dumps({'id':1, 'reply':1001}))

#Score API(점수)(정확성, 효율성, 페널티, 총점)
# score_res = parser.get('/score', headers=header)

# 시나리오 1 테스트용,
Ws = [20, 200]
Hs = [3, 10]
totalDates = [200, 1000]

def main(problem_no):
    # 문제 변수 설정
    W, H, totalDate = Ws[problem_no-1], Hs[problem_no-1], totalDates[problem_no-1]
    
    # 문제 시작
    parser = Parser(token=token, base_url=base_url, verbose=1)
    post_headers = {
        'X-Auth-Token': parser.token,
        'Content-Type': parser.content_type,
    }
    start_res = parser.post('/start', headers=post_headers, data=json.dumps({'problem': problem_no}))
    # print(f'start_res : {start_res}')

    # 헤더 설정
    auth_key = start_res['auth_key']
    headers = {
        'Authorization': auth_key,
        'Content-Type': parser.content_type,
    }

    # 오늘 날짜 설정
    todayNum = 1
    # 사용할 변수 설정
    HotelRooms = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(totalDate+300)]
    WaitingLine = [] # (객실 수, 유통기한, 체크 인 날짜, 체류 기간, 체크 아웃 날짜, id)
    forsimul = []
    while todayNum<=totalDate:
        newRequest = parser.get('/new_requests', headers=headers)
        newRequest_res = newRequest['reservations_info']
        for p in newRequest_res:
            WaitingLine.append([p["amount"], min(p["check_in_date"]-1, todayNum+14), p["check_in_date"], p["check_out_date"]-p["check_in_date"], p["check_out_date"], p["id"], p["amount"]*(p["check_out_date"]-p["check_in_date"])])
            # if p['amount']>=13:
            #     print("이것이 성수기?")
        WaitingLine.sort(key = lambda x: (-x[0],-x[5], x[1], x[2], -x[3], -x[4]))
        
        comp = deque()
        for p in range(len(WaitingLine)):
            am, st, ed, wid = WaitingLine[p][0], WaitingLine[p][2], WaitingLine[p][4], WaitingLine[p][5]
            f = 0
            # 인간 machine learning hard coding
            if problem_no==1:
                if am <=2 and WaitingLine[p][1]-todayNum >=3:
                    continue
                elif am <=3 and WaitingLine[p][1]-todayNum >=12:
                    continue
            if problem_no==2:
                if am <=2 and WaitingLine[p][1]-todayNum >=3:
                    continue
            # elif am <=4 and WaitingLine[p][1]-todayNum >=8:
            #     continue
            # elif am <=6 and WaitingLine[p][1]-todayNum >=12:
            #     continue
            if WaitingLine[p][1]-todayNum <0:
                comp.appendleft([p, 0, 0, 0])
                continue
            for h in range(H):
                startRoom = 0
                while startRoom<W-am+1:
                    flag2 = 0
                    for k in range(am):
                        for d in range(st, ed):
                            if HotelRooms[d][h][startRoom+k]:
                                flag2 = 1
                                startRoom += k+1
                                break
                        if flag2:
                            break

                    else:
                        f=1
                        for d2 in range(st, ed):
                            for k2 in range(am):
                                HotelRooms[d2][h][startRoom+k2] = 1
                        comp.appendleft([p, 1000*(h+1)+(startRoom+1), st, 1])
                    if f:
                        break
                if f:
                    break
            if f==0:
                comp.appendleft([p, 1000*(h+1)+(startRoom+1), st, 0])

        # print(f'WaitingLine : {WaitingLine}')
        getaccep = []
        for p in range(len(comp)):
            tmp = WaitingLine.pop(comp[p][0])
            if comp[p][3]:
                getaccep.append({'id': tmp[5], 'reply':'accepted'})
                forsimul.append([{"id":tmp[5], "room_number":comp[p][1]}, comp[p][2]])
            else:
                getaccep.append({'id': tmp[5], 'reply':'refused'})
        reply_res = parser.put('/reply', headers=headers, data=json.dumps({"replies": getaccep}))
        # print(reply_res)

        # print(f'일단 승락: {forsimul}')
        forreq = []
        for p in range(len(forsimul)-1, -1, -1):
            if forsimul[p][1] == todayNum:
                forreq.append(forsimul.pop(p)[0])
        # print(f'오늘 입장: {forreq}')
        simulate_res = parser.put('/simulate', headers=headers, data=json.dumps({"room_assign":forreq}))
        # print(simulate_res)
        todayNum +=1

    score_res = parser.get('/score', headers=headers)
    print(score_res)


main(1)
main(2)
```

