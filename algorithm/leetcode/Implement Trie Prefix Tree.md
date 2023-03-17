# Implement Trie Prefix Tree

```python
class Trie:

    def __init__(self):
        self.trieDic = {}
        

    def insert(self, word: str) -> None:
        cur = self.trieDic
        for p in range(len(word)):
            if cur.get(word[p]):
                cur = cur[word[p]]
            else:
                cur.update({word[p]:{}})
                cur = cur[word[p]]
        cur.update({0:1})


        

    def search(self, word: str) -> bool:
        cur = self.trieDic
        for p in range(len(word)):
            if cur.get(word[p]):
                cur = cur[word[p]]
            else:
                return False
        else:
            if cur.get(0):
                return True
            else:
                return False

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trieDic
        for p in range(len(prefix)):
            if cur.get(prefix[p]):
                cur = cur[prefix[p]]
            else:
                return False
        else:
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

