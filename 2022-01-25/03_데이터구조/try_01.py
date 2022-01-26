try:
    num = input('숫자 입력: ')
    print(int(num))
except ValueError as e:
    print(f'{e}, 숫자가 입력되지 않았습니다.')
