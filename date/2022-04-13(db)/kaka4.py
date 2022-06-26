food_times, k = [3, 1, 1, 2], 7

if sum(food_times) <= k:
    answer = -1
food = []
for q in range(len(food_times)):
    food.append([food_times[q], q+1, 0])  # [음식 시간, 음식 인덱스, 먹는데 걸릴 시간]
food.sort()
print(food)
tmp_time = 0
tmp_food = 0
q = 0
while 1:
    tmp_time = (food[q][0]-tmp_food)*(len(food)-q)
    if tmp_time > k:
        idx = food[q][1]
        break
    tmp_food = food[q][0]
    food[q][2] += tmp_time
    food.pop(0)
    print(food)
    k -= tmp_time

print(idx, k)
food.sort(key= lambda x: x[1])
answer = food[k%len(food)][1]
print(answer)