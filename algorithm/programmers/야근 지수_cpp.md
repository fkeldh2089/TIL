# 야근 지수



```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


long long solution(int n, vector<int> works) {
    long long answer = 0;
    long long cnt = 0;
    works.push_back(0);
    sort(works.begin(), works.end());
    while(works.size()!=1){
        long long tmp = works.back();
        works.pop_back();
        cnt += 1;
        long long mn = tmp-works.back();
        // cout<< cnt<<" "<<tmp<<" "<<mn<<endl;
        if(cnt*mn<n){
            n -= cnt*mn;
        }else if(cnt*mn==n){
            answer += works.back()*works.back() *cnt;
            break;
        }else{
            long long re = n/cnt;
            long long ma1 = n % cnt;
            long long ma2 = cnt - ma1;
            // cout << "여기가 :"<<re<<" "<<ma1<<endl;
            answer += (tmp-re)*(tmp-re)*ma2;
            answer += (tmp-re-1)*((tmp-re)-1)*ma1;
            break;
        }
    }
    // cout << answer<<endl;
    for(int i =0;i<works.size();i++){
        answer += works[i]*works[i];
        // cout << works[i] << " ";
    }

    return answer;
}
/*
테스트 1 〉	통과 (0.02ms, 3.63MB)
테스트 2 〉	통과 (0.01ms, 4.15MB)
테스트 3 〉	통과 (0.01ms, 3.68MB)
테스트 4 〉	통과 (0.01ms, 4.14MB)
테스트 5 〉	통과 (0.01ms, 3.64MB)
테스트 6 〉	통과 (0.01ms, 3.67MB)
테스트 7 〉	통과 (0.01ms, 4.21MB)
테스트 8 〉	통과 (0.03ms, 3.7MB)
테스트 9 〉	통과 (0.04ms, 4.22MB)
테스트 10 〉	통과 (0.01ms, 4.16MB)
테스트 11 〉	통과 (0.01ms, 4.21MB)
테스트 12 〉	통과 (0.01ms, 4.2MB)
테스트 13 〉	통과 (0.01ms, 3.68MB)
효율성  테스트
테스트 1 〉	통과 (0.09ms, 3.79MB)
테스트 2 〉	통과 (0.11ms, 3.81MB)
```

