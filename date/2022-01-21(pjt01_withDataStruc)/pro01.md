# 과정

## pro a.

목표 : 샘플 영화데이터가 주어집니다. 이중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완 성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

1. 먼저 입력되는 값이 무엇인지 정확하게 파악해야 앞으로의 코드를 생각할 수 있을 것 같았다.
 - `print(movie_dict)`를 통해 어떤 식으로 이루어졌는지 파악했다.
2. 반복문을 사용하여 귀찮은 타이핑을 피할 수 있을까 고민하였지만 일단 요구되는 출력 사항을 내보고 생각하기로 하였다.
   - 일단 생각한 것은 일일이 타자를 쳐서 집어넣는 것이었다.
 ```python
 def movie_info(movie):
    id_1 = movie.get('id')
    tit = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')
   
    result = {
   
        'genre_ids' : genre_ids,
        'id' : id_1,
        'overview' : overview,
        'poster_path' : poster_path,
        'title' : tit,
        'vote_average' : vote_average
        
    }
    return result
 ```

​	이 경우 원하는 출려과 (1){ 이후 \n이 없다. (2)id가 [80,18]이 아닌 [18,80]이 나온다는 결과가 나왔다.

(2) 에 대해서는 기존에 짜두었던 리스트를 크기순으로 정렬하는 알고리즘을 적용하여 해결하였다. - 제거

```python
    """
    k = 1
    l = len(genre_ids)
    numbers = genre_ids
    
    while(k): 
        for i in range(l-1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

            for p in range(l - 1):
                if numbers[p] < numbers[p + 1]:
                    k = 1
                    break
            else:
                k = 0
   """
```

하지만 (1)의 경우는 dictionary에 이스케이프 시퀀스 `\n`을 넣어 보았으나 오류가 발생하였다.

다음 문제 진행에 큰 악영향이 없다고 판단하여 일단 진행하도록 하였다.

## pro b.

목표 : 이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완 성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

1. 먼저 gen list를 `print`를 통해 확인하여, dictionary를 원소로 갖는 list임을 확인 하였다.
2. 이 문제에서 원하는 것은 genres_id를 genres_name으로 전환하는 것이기 때문에 80과 18에 각각 'Crime'과 'Drama'가 들어가면 될것이다.
3. 어떻게 넣는가? 간단하게 다음과 같은 코드를 짰다.

```python
	# 장르 아이디를 문자로 전환하자
    gen = []#장르 이름이 들어갈 list 생성

    for i in numbers:#장르 id에 대하여
        for p in genres_list:
            if i == p['id']:#genres_list에 같은 id를 찾으면
                gen.append(p['name'])#gen에 id에 해당하는 name 추가
```

4. 결과적으로 아래와 같은 함수를 완성하였다.

```python
def movie_info(movie, genres):
    id_1 = movie.get('id')#하나씩 값을 받는다.
    tit = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')
"""
    # genre_id를 내림차순으로 정리하도록 한다. - 제거
    k = 1
    l = len(genre_ids)
    numbers = genre_ids
    
    while(k):
        for i in range(l-1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

            for p in range(l - 1):
                if numbers[p] < numbers[p + 1]:
                    k = 1
                    break
            else:
                k = 0
"""
    # 장르 아이디를 문자로 전환하자
    gen = []#장르 이름이 들어갈 list 생성

    for i in numbers:#장르 id에 대하여
        for p in genres:
            if i == p['id']:#genres_list에 같은 id를 찾으면
                gen.append(p['name'])#gen에 id에 해당하는 name 추가



    # 반환할 dictionary를 만든다.
    result = {
        
        'genre_ids' : gen,
        'id' : id_1,
        'overview' : overview,
        'poster_path' : poster_path,
        'title' : tit,
        'vote_average' : vote_average

    }
    return result 
```



a와 b 를 살펴보니 입력이 80, 18로 들어온 것이 아닌 18, 80으로 들어와서 정렬문 제거, 입 출력 모두 같은 순서이다.



## pro c.

목표 : TMDB기준 평점이 높은 20개의 영화데이터가 주어집니다. 이 중 서비스 구성에 필요한 정 보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용됩니다 

1. `print`문을 통해 movies를 확인하였다. list 안에 dictionary가 여럿 있었다.
2. 문제가 원하는 것은 이것을 pro.c와 같이 정리하여 하나의 리스트 안에 넣는 것이므로 다음과 같은 코드를 썼다.

```python
def movie_info(movies, genres):
    movie_lists = []#반환할 리스트 생성
    tmp = {}#임시 dictionary
    for i in movies:#받는 movies list에 대하여
        tmp = movies_info(i, genres)#각 요소들을 problem_b에서의 함수로 정리한 후
        movie_lists.append(tmp)# 반환할 리스트에 넣어 버린다.

    return movie_lists
```

처음 pro a, pro b 에서 for문을 통해 genre_id를 정리할 때에는 터미널이 멈춰버렸다. 오류 원인 조차 찾기 힘들어, 먼저 반복문에 문제가 있나 for문을 제거 하고 동작시키자 원활히 동작하였다. 이 후 정렬 코드를 제거하였다.



## pro d.

목표 : 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니티 서비스에서 메인 페 이지 기본정보로 사용됩니다. 

1. a먼저 `print`를 통하여 movies_list를 확인 하였다. 이후 data의 하위에 경로들을 파악하였다.
2. 먼저 json을 불러올 수 있는지 확인하였다.

```python
    a = open('data/movies/13.json', encoding = 'UTF8')
    b = json.load(a)
    print(b['revenue'])
```

3. 불러와지는 것을 확인 한 후에 반복문을 통해 각각의 id에 맞는 영화의 revenue를 비교하는 코드를 짰다.

```python
def max_revenue(movies):
    #a = open('data/movies/13.json', encoding = 'UTF8')
    #b = json.load(a)
    #print(b['revenue'])

    k = 0
    
    for i in movies:
        a = open('data/movies/' + str(i['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        #print(a)
        b = json.load(a)

        if k <= b['revenue']:# 큰 revenuer값을 k에 대입
            k = b['revenue']
            k2= i['title']




    return k2#최대값 반환
```

4. 왜인지 코드는 똑같이 짰었는데, 안되다가 됐다.





## pro e.

목표 : 세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉 한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용됩니다. 

1. 먼저 relase date의 형식을 확인한다. `1994-07-06`인 str으로, 총 10글자임을 확인하였다.
2. 즉, 달 부분이 12이면 12월에 출시되었음을 알 수 있다.
3. 슬라이스 함수를 통해 [5:7] == 12 이면 제목을 가져오면 될듯 하다

```
def dec_movies(movies):
    k = 0
    ml = []#반환할 list
    
    for i in movies:
        a = open('data/movies/' + str(i['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        #print(a)
        b = json.load(a)
        #print(b['release_date'][5:7])

        if b['release_date'][5:7] == '12':# 12월달인지 확인 후 추가
            ml.append(i['title'])




    return ml  
```

성공!



# 고찰

1. 저 출력예시처럼 아래와 같은 출력을 만들고 싶었으나, 아래의 pprint문을 건들지 않고서는 힘들어 보였다. 방법이 있나 모르겠다.

```
[
{
내용
}
]
```

2. pro d. 에서 같은 코드를 쓴 것 같은 데, 한참을 돌아가지 않았다. 아마 내 욕심에 코드를 단계단계 밟지 않고 한번에 써서 오류가 어디서 발생하는지 제대로 파악도 못했다. 아예 다 지워버리고 하나씩 `print`를 써가며 출력을 확인하며 하니 코드를 완성하는데 시간차이도 크게 나지 않았지만 정확도나, 오류 발생 지점을 찾는 일이 쉽다는 점에서 좋았다.
3. 시간이 주어지는 대로 예외케이스들이 있는지를 확인해 봐야하겠다. 짧은 시간동안 만든 것은 아니지만, 예제로 주어진 출력으로 확인 할 수 있는 것에도 한계가 있고, 프로그램을 구현하면서 주어진 명세서의 출력 예시대로 만드려고 하다가, 이 input에만 작동하는 프로그램을 만든 것 같은 불안감도 있다.
3.  마지막에 출력 요구사항을 제대로 읽어 보지 않아, 이상한 출력값을 내줄뻔 했다. 주의하도록 해야한다.



# 결과

1. problem_a

```python
import json
from pprint import pprint

from pyparsing import indentedBlock


def movie_info(movie):
    id_1 = movie.get('id')#하나씩 값을 받는다.
    tit = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    




    # 반환할 dictionary를 만든다.
    result = {

        'genre_ids' : genre_ids,
        'id' : id_1,
        'overview' : overview,
        'poster_path' : poster_path,
        'title' : tit,
        'vote_average' : vote_average

    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



2. problem_b

```python
import json
from pprint import pprint


def movie_info(movie, genres):
    id_1 = movie.get('id')#하나씩 값을 받는다.
    tit = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')


    # 장르 아이디를 문자로 전환하자
    gen = []#장르 이름이 들어갈 list 생성

    for i in genre_ids:#장르 id에 대하여
        for p in genres:
            if i == p['id']:#genres_list에 같은 id를 찾으면
                gen.append(p['name'])#gen에 id에 해당하는 name 추가



    # 반환할 dictionary를 만든다.
    result = {
        
        'genre_ids' : gen,
        'id' : id_1,
        'overview' : overview,
        'poster_path' : poster_path,
        'title' : tit,
        'vote_average' : vote_average

    }
    return result  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```



3. problem_c

```
import json
from pprint import pprint

def movies_info(movie, genres):
    id_1 = movie.get('id')#하나씩 값을 받는다.
    tit = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    

    # 장르 아이디를 문자로 전환하자
    gen = []#장르 이름이 들어갈 list 생성

    for i in genre_ids:#장르 id에 대하여
        for p in genres:
            if i == p['id']:#genres에 같은 id를 찾으면
                gen.append(p['name'])#gen에 id에 해당하는 name 추가



    # 반환할 dictionary를 만든다.
    result = {
        
        'genre_ids' : gen,
        'id' : id_1,
        'overview' : overview,
        'poster_path' : poster_path,
        'title' : tit,
        'vote_average' : vote_average

    }
    return result  

def movie_info(movies, genres):
    movie_lists = []#반환할 리스트 생성
    tmp = {}#임시 dictionary
    for i in movies:#받는 movies list에 대하여
        tmp = movies_info(i, genres)#각 요소들을 problem_b에서의 함수로 정리한 후
        movie_lists.append(tmp)# 반환할 리스트에 넣어 버린다.

    return movie_lists


        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```



4. problem_d

```
import json


def max_revenue(movies):
    #a = open('data/movies/13.json', encoding = 'UTF8')
    #b = json.load(a)
    #print(b['revenue'])

    k = 0
    
    for i in movies:
        a = open('data/movies/' + str(i['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        #print(a)
        b = json.load(a)

        if k <= b['revenue']:# 큰 revenuer값을 k에 대입
            k = b['revenue']
            k2= i['title']




    return k2#최대값 반환
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```



5. problem_e

```
import json


def dec_movies(movies):
    k = 0
    ml = []#반환할 list
    
    for i in movies:
        a = open('data/movies/' + str(i['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        #print(a)
        b = json.load(a)
        #print(b['release_date'][5:7])

        if b['release_date'][5:7] == '12':# 12월달인지 확인 후 추가
            ml.append(i['title'])




    return ml  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```

