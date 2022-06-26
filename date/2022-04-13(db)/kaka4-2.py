import heapq

h = []
food_times, k = [3, 1, 2], 5
for q in range(len(food_times)):
    heapq.heappush(h, [food_times[q], q+1])
print(h)
total_elapsed_time = 0

# 현재까지 각 음식을 먹는 데 걸린 최대시간
# 예를들어 food_times: [1,3,5,9]이고 현재 5까지 진행됐으면 5입니다
each_eating_time = 0

length = len(h)  # 음식 개수
while length * (h[0][0] - each_eating_time) < (k - total_elapsed_time):
    total_elapsed_time += length * (h[0][0] - each_eating_time)
    each_eating_time += (h[0][0] - each_eating_time)

    heapq.heappop(h)
    length -= 1

result = sorted(h, key=lambda x: x[1])
print(result)
print(result[(k - total_elapsed_time) % len(h)][1])