input = "140000"


n = len(input)

def rec(k):
    if k == 3:
        return 1
    elif k <3 :
        return 0
    else:
        return rec(k-1)*10 + 10**(k-3) -rec(k-2)
    
# def counts(k):
#     if k

ret = rec(n)
print(ret)