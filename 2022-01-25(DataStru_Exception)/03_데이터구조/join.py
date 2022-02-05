# 1. 요소가 문자열인 경우
# numbers = ['1', '2', '3']
# # 출력 : 1 2 3
# # 1. 반복문
# # for number in numbers:
# #     print(number, end=' ')
# # 2. join (string 메서드)
# print(' '.join(numbers))

# 2. 요소가 문자열이 아닌 경우
numbers = [1, 2, 3]
# print(' '.join(numbers)) # TypeError: sequence item 0: expected str instance, int found
print(' '.join(map(str, numbers))) 