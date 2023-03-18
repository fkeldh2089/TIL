# Design browser history

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.idx = 0
        self.his = [homepage]

    def visit(self, url: str) -> None:
        self.his = self.his[:self.idx+1]
        self.his.append(url)
        self.idx += 1
        # print(self.his[self.idx])

    def back(self, steps: int) -> str:
        if self.idx<steps:
            self.idx = 0
        else:
            self.idx -= steps
        # print(self.his[self.idx])
        return self.his[self.idx]
        

    def forward(self, steps: int) -> str:
        if self.idx+steps>=len(self.his):
            self.idx = len(self.his)-1
        else:
            self.idx += steps
        # print(self.his[self.idx])
        return self.his[self.idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

