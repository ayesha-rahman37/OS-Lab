process = [["P1", 3, 1],
           ["P2", 2, 4],
           ["P3", 3, 6],
           ["P4", 1, 3],
           ["P5", 4, 2],
           ["P6", 6, 1]]

n = len(process)

t_tat = 0
t_wt = 0

# [PID, AT, BT, CT, TAT, WT, Remaining Time]
for p in process:
    p.append(-1)       # CT
    p.append(-1)       # TAT
    p.append(-1)       # WT
    p.append(p[2])     # Remaining Time = BT

cnt = 0
completed = 0

while completed < n:

    idx = -1
    min_rt = float('inf')

    # Select process with shortest remaining time
    for i in range(n):
        at = process[i][1]
        rt = process[i][6]

        if at <= cnt and rt > 0 and rt < min_rt:
            min_rt = rt
            idx = i

    # CPU idle
    if idx == -1:
        cnt += 1
        continue

    # Execute for 1 time unit
    process[idx][6] -= 1
    cnt += 1

    # Check whether process is completed
    if process[idx][6] == 0:

        at = process[idx][1]
        bt = process[idx][2]

        ct = cnt
        tat = ct - at
        wt = tat - bt

        process[idx][3] = ct
        process[idx][4] = tat
        process[idx][5] = wt

        t_tat += tat
        t_wt += wt

        completed += 1

# Sort by Process ID
process.sort(key=lambda x: int(x[0][1:]))

print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in process:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

avg_tat = t_tat / len(process)
avg_wt = t_wt / len(process)

print("\nAvgTAT =", avg_tat)
print("AvgWT  =", avg_wt)