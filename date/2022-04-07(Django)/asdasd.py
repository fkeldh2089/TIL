msg = "TOBEORNOTTOBEORTOBEORNOT"
answer = []
dic = {}
msg_ls = []
for q in range(65, 91):  # 사전 생성
    dic.update({chr(q):q-64})
for q in range(len(msg)):  # 메세지를 숫자로 변환
    msg_ls.append(dic[msg[q]])

i = 0
inum = 27
while 1:
    if i < len(msg)-1:
        if dic.get(100*msg_ls[i]+msg_ls[i+1]):
            msg_ls[i:i+2] = [0, dic.get(100*msg_ls[i]+msg_ls[i+1])]
            i+=1
        else:
            dic.update({100*msg_ls[i]+msg_ls[i+1]:inum})
            inum += 1
            i += 1
    else:
        break
for q in range(len(msg_ls)):
    if msg_ls[q] == 0:
        pass
    else:
        answer.append(msg_ls[q])
print(answer)