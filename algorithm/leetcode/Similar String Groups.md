# Similar String Groups

```python
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = set(strs)
        dic = defaultdict(list)
        for str in strs:
            vec = [0] * 26
            for c in str:
                vec[ord(c) - 97] += 1
            dic[tuple(vec)].append(str)
        
        def find_parent(a):
            if parents[a] == a:
                return a
            parents[a] = find_parent(parents[a])
            return parents[a]
        
        def union(a, b):
            a, b = find_parent(a), find_parent(b)
            if a < b:
                parents[b] = a
            else:
                parents[a] = b
        
        def numGroup():
            for i in range(len(parents)):
                find_parent(i)
            return len(set(parents))
        
        def isAdjacent(word1, word2):
            cnt = 0
            for i, c in enumerate(word1):
                if c != word2[i]:
                    cnt += 1
                if cnt >= 3:
                    return False
            return True
        
        ret = 0
        for _, strs in dic.items():
            parents = [i for i in range(len(strs))]
            for i in range(len(strs)):
                for j in range(i+1, len(strs)):
                    if isAdjacent(strs[i], strs[j]):
                        union(i, j)
            ret += numGroup()
        return ret
```

