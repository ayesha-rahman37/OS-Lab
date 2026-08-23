process = [["P1", 3, 1],
           ["P2", 2, 4],
           ["P3", 3, 6],
           ["P4", 1, 3],
           ["P5", 4, 2],
           ["P6", 6, 1]]

cnt = 0
t_tat = 0
t_wt = 0

completed = 0
n = len(process)

# [PID, AT, BT, CT, TAT, WT, Done]
for p in process:
    p.append(-1)
    p.append(-1)
    p.append(-1)
    p.append(False)

while completed < n:

    idx = -1
    min_bt = float('inf')

    # Select shortest burst time among arrived processes
    for i in range(n):
        at = process[i][1]
        bt = process[i][2]
        done = process[i][6]

        if not done and at <= cnt and bt < min_bt:
            min_bt = bt
            idx = i

    # If no process has arrived
    if idx == -1:
        next_at = float('inf')

        for i in range(n):
            if not process[i][6] and process[i][1] < next_at:
                next_at = process[i][1]

        cnt = next_at
        continue

    at = process[idx][1]
    bt = process[idx][2]

    # Non-preemptive execution
    cnt += bt
    ct = cnt

    tat = ct - at
    wt = tat - bt

    process[idx][3] = ct
    process[idx][4] = tat
    process[idx][5] = wt
    process[idx][6] = True

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