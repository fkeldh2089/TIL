from jose import JWTError, jwt

SECRET="Secret"

def encodejwt(n):
    json = {'sub': n, 'iss': 'ollenge.com', 'exp': 1768646071, 'iat': 1667350071}
    tk = jwt.encode(json, SECRET, algorithm="HS512")
    print(tk)
    print(type(tk))
    return tk

def decodejwt(tk:str):
    decoded = jwt.decode(tk, SECRET, algorithms="HS512")  # dict
    print(decoded)

for i in range(29,30):
    a = encodejwt(str(i))
    decodejwt(a)