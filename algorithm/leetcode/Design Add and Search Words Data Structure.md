# Design Add and Search Words Data Structure

```python
from collections import deque


class WordDictionary:

    def __init__(self):
        self.wordDic = {}
        

    def addWord(self, word: str) -> None:
        cur = self.wordDic
        for p in range(len(word)):
            if cur.get(word[p]):
                cur = cur[word[p]]
            else:
                cur.update({word[p]:{}})
                cur = cur[word[p]]
        cur.update({1:1})
            
        

    def search(self, word: str) -> bool:
        # print(self.wordDic)
        q = deque()
        q.append(self.wordDic)
        for p in range(len(word)):
            if word[p] == ".":
                q2 = deque()
                while q:
                    cur = q.pop()
                    for key, it in cur.items():
                        if it != 1:
                            q2.appendleft(it)
                if q2:
                    q = q2
                else:
                    return False
                
            else:
                q2 = deque()
                while q:
                    cur = q.pop()
                    # print(cur)
                    if cur.get(word[p]) and cur[word[p]] != 1:
                        q2.appendleft(cur[word[p]])
                if q2:
                    q = q2
                else:
                    return False
        while q:
            cur = q.pop()
            if cur.get(1):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

