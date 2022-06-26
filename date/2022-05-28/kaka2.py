def solution(play_time, adv_time, logs):
    answer = ''

    ht, mt, st = play_time.split(':')
    whole_time = int(ht) * 3600 + int(mt) * 60 + int(st)
    wholeTimeList = [0] * (whole_time + 1)

    ht, mt, st = adv_time.split(':')
    ad = int(ht) * 3600 + int(mt) * 60 + int(st)

    startPoint = whole_time - ad
    for p in logs:
        startTime, endTime = p.split('-')
        ht, mt, st = startTime.split(':')
        wholeTimeList[(int(ht) * 3600 + int(mt) * 60 + int(st))] += 1
        # if (int(ht)*3600 + int(mt)*60 + int(st)) < whole_time-ad:
        #     startPoint.append(int(ht)*3600 + int(mt)*60 + int(st))
        ht, mt, st = endTime.split(':')
        wholeTimeList[(int(ht) * 3600 + int(mt) * 60 + int(st))] -= 1

    # startPoint.sort(reverse=True)
    for p in range(whole_time):
        wholeTimeList[p + 1] += wholeTimeList[p]
    print(wholeTimeList)

    i = 0
    j = ad
    mn = sum(wholeTimeList[i:j])
    mnum = 0
    while j < whole_time:
        i += 1
        j += 1
        mn -= wholeTimeList[i-1]
        mn += wholeTimeList[j]
        # print(mn)
        if mn > mnum:
            end = i
            mnum = mn
            print(end)
    ST = end % 60
    mn -= ST
    MT = end % 3600
    mn -= MT
    MT = MT // 60
    HT = end // 3600
    # print(HT, MT, ST)

    answer = str(HT).zfill(2) + ':' + str(MT).zfill(2) + ':' + str(ST).zfill(2)
    return answer

play_time ="02:03:55"
adv_time ="00:14:15"
logs =["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))