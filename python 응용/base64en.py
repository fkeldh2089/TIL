import base64
import sys
sys.stdout = open('base64.txt','w', encoding='utf-8')

with open('4.jpg', 'rb') as img:
    base64_string = base64.b64encode(img.read())
print(base64_string)