processes = [
    {"pid": "P1", "at": 3, "bt": 3, "priority": 1},
    {"pid": "P2", "at": 0, "bt": 4, "priority": 3},
    {"pid": "P3", "at": 2, "bt": 2, "priority": 2},
    {"pid": "P4", "at": 1, "bt": 3, "priority": 1},
    {"pid": "P5", "at": 2, "bt": 4, "priority": 0}
]

for p in processes:
    p["rt"] = p["bt"]

time = 0
completed = 0
n = len(processes)
gantt = []

while completed < n:
    ready = [
        p for p in processes
        if p["at"] <= time and p["rt"] > 0
    ]

    if not ready:
        time += 1
        continue

    # Smaller priority number means higher priority
    current = min(
        ready,
        key=lambda p: (p["priority"], p["at"], p["pid"])
    )

    start = time
    current["rt"] -= 1
    time += 1

    if gantt and gantt[-1][2] == current["pid"]:
        gantt[-1] = (gantt[-1][0], time, current["pid"])
    else:
        gantt.append((start, time, current["pid"]))

    if current["rt"] == 0:
        current["ct"] = time
        current["tat"] = current["ct"] - current["at"]
        current["wt"] = current["tat"] - current["bt"]
        completed += 1


for start, end, pid in gantt:
    print(f"{start} -- {pid} -- {end}")

print("\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")

for p in sorted(processes, key=lambda p: p["pid"]):
    print(
        f'{p["pid"]}\t{p["at"]}\t{p["bt"]}\t'
        f'{p["priority"]}\t\t{p["ct"]}\t'
        f'{p["tat"]}\t{p["wt"]}'
    )

avg_tat = sum(p["tat"] for p in processes) / n
avg_wt = sum(p["wt"] for p in processes) / n

print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
print(f"Average Waiting Time = {avg_wt:.2f}")