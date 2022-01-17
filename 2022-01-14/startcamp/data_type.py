# 숫자
number = 3
print(type(number))

# 문자
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환
string_number = '3'
#print(string_number + 5)
print(int(string_number) + 5)

# f-string / string interpolation
name = '홍길동'
print(f'{name}입니다. 반갑습니다.')


"""
리스트
"""
# 리스트 선언
my_list = ['java', 'django']

# 리스트 원소 접근
print(my_list[0])

# 리스트 원소 변경
my_list[0] = 'python'

# 리스트 원소 접근
print(my_list[0])

# 리스트 길이
print(len(my_list))


"""
리스트 실습
"""
# 1. 어제 먹은 음식들로 채워진 리스트를 만들어보시오.
eat=['김밥','부대찌개','사골국']
# 2. 첫번째 음식을 출력하시오.
print(eat[0])
# 3. 두번째 음식을 초밥으로 바꾸시오.
eat[1]='초밥'
print(eat)
"""
딕셔너리
"""
# 딕셔너리 선언
my_home = {
    'location': 'seoul',
    'area-code': '02',
}

# 딕셔너리 원소 접근
print(my_home['location'])
#print(my_home['name'])
print(my_home.get('location'))
#print(my_home.get('name'))

# 딕셔너리 원소 변경
my_home['location'] = 'gumi'
print(my_home['location'])

"""
딕셔너리 실습1
"""
# 1-1. 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만들어보시오.
# (name, age,s msg)
me = {
    'name': 'hong',
    'age': 25,
    's_smg':'hihi'
}
# 1-2. my_info 딕셔너리에서 나이만 출력하시오.
print(me.get('age'))

"""
딕셔너리 실습2
"""

coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])

"""
list & dict
"""
movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극', 'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])
# 2. 다음 movie의 감독의 영어 이름을 출력하시오.
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
# 3. 다음 movie의 배우의 인원을 출력하시오.
print(len(movie['movieInfo']['actors']))