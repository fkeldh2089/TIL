rec = [[0, 0], [1, 10], [6, 13], [0, 3]]

def checkcross(a, b, c, d):
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c
    d1, d2 = d
    if a1!=b1:
        p1 = (a2 - b2)/(a1 - b1)
        q1 = a1*((a2-b2)/(b1-a1))+a2
        lin1 = [1, p1, q1]
    else:
        p1 = -1
        q1 = a1
        lin1 = [0, p1, q1]
    
    if c1 != d1:
        p2 = (c2 - d2)/(c1 - d1)
        q2 = c1*((c2-d2)/(d1-c1))+c2
        lin2 = [1, p2, q2]
    else:
        p2 = -1
        q2 = c1
        lin2 = [0, p2, q2]

    lin3 = []
    for p in range(3):
        lin3.append(lin1[p]-lin2[p])
    
    x, y = a
    cal1 = -lin3[0]*y + lin3[1]*x+lin3[2]
    x, y = b
    cal2 = -lin3[0]*y + lin3[1]*x+lin3[2]
    cro = cal1*cal2
    if cro >= 0:
        return True
    else:
        return False

print(checkcross(*rec))
# print((rec[1:]+[rec[0]]))
print(checkcross(*(rec[1:]+[rec[0]])))