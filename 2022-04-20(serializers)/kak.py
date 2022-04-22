def ans(p):
    cnt = 0
    f = 0
    u = ''
    v = ''
    u2 = ''
    if len(p) == 0:
        return ''
    for q in range(len(p)):
        u += p[q]
        if p[q] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            f = 1
        elif cnt == 0:
            if f == 0:
                if q == len(p)-1:
                    return p
                v = p[q+1:]
                return u + ans(v)
            else:
                v = p[q + 1:]
                for q2 in range(1, len(u)-1):
                    if u[q2] == '(':
                        u2 += ')'
                    else:
                        u2 += '('
                return '('+ans(v)+')'+ u2

tmp = ans("(()())()")
print(tmp)
