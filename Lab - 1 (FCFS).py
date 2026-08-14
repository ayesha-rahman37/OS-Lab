process = [["P1", 3, 3],
           ["P2", 2, 1],
           ["P3", 5, 2],
           ["P4", 0, 3],
           ["P5", 1, 2]]

cnt = 0
t_tat = 0
t_wt = 0

# Sort according to Arrival Time
process.sort(key=lambda x: x[1])

# FCFS calculation
for i in range(len(process)):

    pid = process[i][0]
    at = process[i][1]
    bt = process[i][2]

    # If CPU is idle
    if cnt < at:
        cnt = at

    # Completion Time
    cnt += bt
    ct = cnt

    # Turnaround Time
    tat = ct - at

    # Waiting Time
    wt = tat - bt

    # Store CT, TAT, WT
    process[i].append(ct)
    process[i].append(tat)
    process[i].append(wt)

    t_tat += tat
    t_wt += wt


# Sort again according to Process ID
process.sort(key=lambda x: int(x[0][1:]))

# Print result
print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in process:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")


# Average TAT and WT
avg_tat = t_tat / len(process)
avg_wt = t_wt / len(process)

print("\nAvgTAT =", avg_tat)
print("AvgWT  =", avg_wt)
