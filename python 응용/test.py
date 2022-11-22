from datetime import datetime

now = datetime.now()
print(now.year)
current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
print(current_time)