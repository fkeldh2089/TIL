files = ["img20.JPG", "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
answer = []
namelist = []
for q in range(len(files)):
    f = 0
    HEAD = ''
    NUMBER = ''
    for q1 in range(len(files[q])):
        if files[q][q1].isdigit():
            NUMBER += files[q][q1]
            f = 1
        else:
            if f == 0:
                HEAD += files[q][q1]
    namelist.append([HEAD.lower(), int(NUMBER), q])
namelist.sort()
print(namelist)
for q in range(len(files)):
    answer.append(files[namelist[q][2]])
print(answer)
print("1"+"1")
