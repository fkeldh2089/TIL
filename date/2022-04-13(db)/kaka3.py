pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
word = 'Muzi'
word = word.lower()
pagenum = len(pages)
pagedict = {}
mn = 0
idx = 0
for q in range(pagenum):
    tmp_page = pages[q].split('\n')
    for q1 in range(len(tmp_page)):
        if "https://" in tmp_page[q1]:
            if '<meta' in tmp_page[q1]:
                cnt = 0
                tmp_http = ''
                for q2 in tmp_page[q1]:
                    if q2 == '"':
                        cnt += 1
                    elif cnt == 3:
                        tmp_http += q2
                pagedict[tmp_http]=[q, 0, 0, 0]
            else:
                cnt = 0
                tmp_ahttp = ''
                for q2 in tmp_page[q1]:
                    if q2 == '"':
                        cnt += 1
                    elif cnt == 1:
                        tmp_ahttp += q2
                pagedict[tmp_http].append(tmp_ahttp)
                pagedict[tmp_http][2] += 1
        if word in tmp_page[q1].lower():  # default score
            tmp_word = ''
            for r in tmp_page[q1].lower():
                if r.isalpha():
                    tmp_word += r
                else:
                    if tmp_word == word:
                        pagedict[tmp_http][1] += 1
                    tmp_word = ''
            else:
                if tmp_word == word:
                    pagedict[tmp_http][1] += 1
                tmp_word = ''


for q in pagedict.keys():
    pagedict[q][3] += pagedict[q][1]
    for q1 in range(len(pagedict[q])):
        if pagedict.get(pagedict[q][q1]):
            pagedict[pagedict[q][q1]][3] += (pagedict[q][1]/pagedict[q][2])

for q in pagedict.keys():
    if mn < pagedict[q][3]:
        mn = pagedict[q][3]
        idx = pagedict[q][0]

print(pagedict)
print(idx)