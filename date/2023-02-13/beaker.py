from collections import deque

beakers = [3, 5, 20]
N = 19

def solution(beakers, N):
    a, b, c= beakers
    if b < a:
        a,b = b,a
    qu = deque()
    qu.append([0, 0, 0, 0])
    visited = {}
    while qu:
        A, B, C, cnt = qu.popleft()
        #1 fill a
        a1 = a
        b1 = B
        c1 = C
        cnt1 = cnt+1
        if visited.get((a1, b1, c1)):
            pass
        else:
            if N in (a1, b1, c1):
                return cnt1
            visited.update({(a1, b1, c1):cnt1})
            qu.append([a1, b1, c1, cnt1])

        #2 fill b
        a2 = A
        b2 = b
        c2 = C
        cnt2 = cnt+1
        if visited.get((a2, b2, c2)):
            pass
        else:
            if N in (a2, b2, c2):
                return cnt2
            visited.update({(a2, b2, c2):cnt2})
            qu.append([a2, b2, c2, cnt2])
        #3 a -> b
        b3 = (A+B)%b
        a3 = A+B-b3
        c3 = C
        cnt3 = cnt+1
        if visited.get((a3, b3, c3)):
            pass
        else:
            if N in (a3, b3, c3):
                return cnt3
            visited.update({(a3, b3, c3):cnt3})
            qu.append([a3, b3, c3, cnt3])

        #4 b -> a
        a4 = (A+B)%a
        b4 = A+B-a4
        c4 = C
        cnt4 = cnt+1
        if visited.get((a4, b4, c4)):
            pass
        else:
            if N in (a4, b4, c4):
                return cnt4
            visited.update({(a4, b4, c4):cnt4})
            qu.append([a4, b4, c4, cnt4])

        #5 a -> c
        c5 = (A+C)%c
        a5 = A+C-c5
        b5 = B
        cnt5 = cnt+1
        if visited.get((a5, b5, c5)):
            pass
        else:
            if N in (a5, b5, c5):
                return cnt5
            visited.update({(a5, b5, c5):cnt5})
            qu.append([a5, b5, c5, cnt5])

        #6 c -> a
        a6 = (A+C)%a
        c6 = A+C-a6
        b6 = B
        cnt6 = cnt+1
        if visited.get((a6, b6, c6)):
            pass
        else:
            if N in (a6, b6, c6):
                return cnt6
            visited.update({(a6, b6, c6):cnt6})
            qu.append([a6, b6, c6, cnt6])

        #7 b -> c
        a7 = A
        c7 = (B+C)%c
        b7 = B+C-c7
        cnt7 = cnt+1
        if visited.get((a7, b7, c7)):
            pass
        else:
            if N in (a7, b7, c7):
                return cnt7
            visited.update({(a7, b7, c7):cnt7})
            qu.append([a7, b7, c7, cnt7])

        #8 c -> b
        a8 = A
        b8 = (B+C)%b
        c8 = B+C-b8
        cnt8= cnt+1
        if visited.get((a8, b8, c8)):
            pass
        else:
            if N in (a8, b8, c8):
                return cnt8
            visited.update({(a8, b8, c8):cnt8})
            qu.append([a8, b8, c8, cnt8])

        #9 empty a
        a9 = 0
        b9 = B
        c9 = C
        cnt9= cnt+1
        if visited.get((a9, b9, c9)):
            pass
        else:
            if N in (a9, b9, c9):
                return cnt9
            visited.update({(a9, b9, c9):cnt9})
            qu.append([a9, b9, c9, cnt9])

        #10 empty b
        a10 = A
        b10 = 0
        c10 = C
        cnt10= cnt+1
        if visited.get((a10, b10, c10)):
            pass
        else:
            if N in (a10, b10, c10):
                return cnt10
            visited.update({(a10, b10, c10):cnt10})
            qu.append([a10, b10, c10, cnt10])
        
        #11 empty c
        a11 = A
        b11 = B
        c11 = 0
        cnt11= cnt+1
        if visited.get((a11, b11, c11)):
            pass
        else:
            if N in (a11, b11, c11):
                return cnt11
            visited.update({(a11, b11, c11):cnt11})
            qu.append([a11, b11, c11, cnt11])
    return -1
    

print(solution(beakers,N))