#### python

GIL : Global Interpreter Lock의 약자로 파이썬 인터프리터가 한 스레드만 하나의 바이트코드를 실행 시킬 수 있도록 해주는 Lock

```python
import random
import threading
import time


def working():
    max([random.random() for i in range(500000000)])


# 1 Thread
s_time = time.time()
working()
working()
e_time = time.time()
print(f'{e_time - s_time:.5f}')


# 2 Threads
s_time = time.time()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=working))
    threads[-1].start()

for t in threads:
    t.join()

e_time = time.time()
print(f'{e_time - s_time:.5f}')
```

python은 모든 객체에 대하여 참조횟수를 저장하여, Garbage Collector가 메모리를 관리하는데 사용하고 있음, 하지만, 여러 스레드가 동시에 한 객체에 접근하게 되면 race condition 발생,오류의 위험성이 있기 떄문

