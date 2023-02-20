# Substring with Concatenation of All Words

```python
from collections import deque, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsDic = {}
        wordsCnt = {}
        cnt = 1
        ans = []
        for p in range(len(words)):
            tmp = wordsDic
            K = deque(words[p])
            while K:
                k = K.popleft()
                if K:
                    if tmp.get(k):
                        tmp = tmp[k]
                    else:
                        tmp.update({k:{}})
                        tmp = tmp[k]
                else:
                    if tmp.get(k):
                        wordsCnt[tmp[k]] += 1
                    else:
                        tmp.update({k:cnt})
                        wordsCnt.update({cnt:1})
                        cnt += 1
        qu = deque()
        for p in range(len(s)):
            qu2 = deque()
            st = s[p]
            while qu:
                pro, sco, tot, sta = qu.popleft()
                # print(pro, sco, tot, sta, print(type(pro[st])))
                if pro.get(st):
                    if isinstance(pro[st], int):
                        sco[pro[st]] += 1
                        if sco[pro[st]]>wordsCnt[pro[st]]:
                            pass
                        else:
                            if tot+1 == len(words):
                                ans.append(sta)
                            elif tot+1 < len(words):
                                qu2.append([wordsDic, sco, tot+1, sta])
                            else:
                                pass
                    else:
                        qu2.append([pro[st], sco, tot, sta])
            qu = qu2
            if wordsDic.get(st):
                if isinstance(wordsDic[st], int):
                    sco = defaultdict(int)
                    sco[wordsDic[st]] += 1
                    tot = 0
                    if sco[wordsDic[st]]>wordsCnt[wordsDic[st]]:
                        pass
                    else:
                        if tot+1 == len(words):
                            
                            ans.append(p)
                        elif tot +1<len(words):
                            qu.append([wordsDic, sco, tot+1, p])
                        else: apss
                else:
                    qu.append([wordsDic[st], defaultdict(int), 0, p])
        return ans

        
```

