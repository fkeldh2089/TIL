# Capacity to Ship Packages within D-days

````python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mx = 0
        tot = 0
        for p in range(len(weights)):
            tot += weights[p]
            if weights[p] > mx:
                mx = weights[p]
        l, r = mx, tot
        while l<r:
            f = 1
            a = 0
            mid = (l+r)//2
            cnt = 0
            tmp = mid
            for p in range(len(weights)):
                if tmp < weights[p]:
                    tmp = mid
                    tmp -= weights[p]
                    cnt += 1
                    if cnt > days:
                        f = 0
                        break
                else:
                    tmp -= weights[p]
            if cnt >= days:
                l = mid+1
            else:
                r = mid
                a = 1
        mid = l-1
        f = 0
        # while f==1:
        #     f = 0
        #     mid -= 1
        #     tmp = mid
        #     cnt = 0
        #     for p in range(len(weights)):
        #         if tmp < weights[p]:
        #             tmp = mid
        #             tmp -= weights[p]
        #             cnt += 1
        #             if cnt > days:
        #                 f = 1
        #                 break
        #         else:
        #             tmp -= weights[p]

        while f==0:
            f = 1
            mid += 1
            tmp = mid
            cnt = 0
            for p in range(len(weights)):
                if tmp < weights[p]:
                    tmp = mid
                    tmp -= weights[p]
                    cnt += 1
                    if cnt > days:
                        f = 0
                        break
                else:
                    tmp -= weights[p]
        return mid

````

