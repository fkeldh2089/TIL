a = [100, 10, 1, 5]
b = [100, 10, 1, 5]

# 1. 메서드 (리스트.sort())
# 원본 리스트를 정렬시키고, None를 return
print(a)
print(a.sort())
print(a) # alt + 방향키 : 단축키

print('===============')
# 2. 함수 (sorted(리스트))
# 원본 리스트는 변경 X, 정렬된 리스트를 return
# [1, 5, 10, 100]
print(b)
print(sorted(b))
print(b)


# 정렬을 시키고 싶다.
a = [100, 2]
a.sort() 
# 코드~

b = [100, 2]
b = sorted(b)
# 코드~

print('정렬 및 뒤집기')
a = [100, 2, 6]
a.sort()
a.reverse()
print(a)
