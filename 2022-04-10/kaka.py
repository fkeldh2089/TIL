a = ["word", "war", "warrior", "world", 'wac', 'wacd', 'wo']


def solution(words):
    answer = 0
    words.sort()
    print(words)

    for q in range(len(words)):
        cnt1 = 0
        cnt2 = 0
        if q < len(words[q]) - 1:
            for q1 in range(len(words[q])):  # 뒤의 단어와 비교하였을 때,
                if words[q][q1] == words[q + 1][q1]:
                    cnt1 += 1
                else:
                    break
        if q != 0:
            for q1 in range(len(words[q - 1])):  # 앞의 단어와 비교하였을 떄,
                if words[q - 1][q1] == words[q][q1]:
                    cnt2 += 1
                else:
                    break
            else:  # 전부 같으면, 그것 보다 한글자는 더 쳐야 하므로,,
                cnt2 += 1

        if cnt1 > cnt2:
            answer += cnt1
        else:
            answer += cnt2

    return answer

print(solution(a))