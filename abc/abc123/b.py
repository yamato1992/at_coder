time = 0
dishes = [int(input()) for _ in range(5)]
lead_times = [0] * 5
long_time = 0
last_dish = 0

for i in range(5):
    lead_times[i] = (10 - (dishes[i] % 10)) % 10
    if lead_times[i] > long_time:
        last_dish = i
        long_time = lead_times[i]

for i in range(5):
    time += dishes[i]
    if i != last_dish:
        time += lead_times[i]

print(time)
