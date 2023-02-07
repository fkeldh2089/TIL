# letter combinations of a phone number

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        phoneLetter = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        stack = [""]
        for digit in digits:
            n = int(digit)-2
            stack2 = []
            while stack:
                tmp = stack.pop()
                for p in phoneLetter[n]:
                    tmp2 = tmp + p
                    stack2.append(tmp2)
            stack = stack2
        return stack

```

