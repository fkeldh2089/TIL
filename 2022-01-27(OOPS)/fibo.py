# 4. Module Import
def fibo_recursion(n):
    if n <2:
        return 2
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)
