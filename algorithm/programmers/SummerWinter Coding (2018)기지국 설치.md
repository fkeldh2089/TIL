# Summer/Winter Coding (~2018)기지국 설치

```python
def solution(n, stations, w):
    answer = 0
    stations.append(n+w+1)
    stations.append(n+w+1)
    for p in range(len(stations)-1):
        if p:
            if (stations[p]-w-1)-(stations[p-1]+w)>0:
                answer += ((stations[p]-w-1)-(stations[p-1]+w))//(2*w+1)
                if ((stations[p]-w-1)-(stations[p-1]+w))%(2*w+1):
                    answer += 1
        else:
            if stations[p]-w-1> 0:
                answer += (stations[p]-w-1)//(2*w+1)
                if (stations[p]-w-1)%(2*w+1):
                    answer += 1
        print(p,stations[p], answer)
                
    
    
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.4MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.4MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.4MB)
테스트 20 〉	통과 (0.01ms, 10.4MB)
테스트 21 〉	통과 (0.04ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (11.59ms, 10.6MB)
테스트 2 〉	통과 (13.58ms, 10.5MB)
테스트 3 〉	통과 (12.69ms, 10.6MB)
테스트 4 〉	통과 (11.91ms, 10.6MB)
'''
```

