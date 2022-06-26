1. 

```python
# 1. 평균 점수 구하기
def get_dict_avg(n):
    sum = 0
    l = 0
    avg = 0
    
    for i in n: # 과목 수
        l += 1
        
    for i in n: # 합계
        sum += n[i]
        
    avg = sum / l
    return avg
```



2. 

```python
# 2. 혈액형 분류하기
def count_blood(n):
    so = ['A', 'B', 'O', 'AB'] # 모든 혈액형을 갖는 list
    dic = {}
    for i in so: # 혈액형에 대하여
        dic.update({i : n.count(i)}) # 혈액형과 그 수를 갖는 dictionary를 구성
    return dic
        
```
