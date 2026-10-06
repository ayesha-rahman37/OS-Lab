processes = [0, 41, 30, 100, 62, 51, 20]
head = 70 
head_move = 0

def fcfs_unordered(prpcesses, head):
    head_move = 0

    print("Processes: ", head, end = " ")


for i in processes:
    movement = abs(i - head)
    head_move += movement
    head = i
    print("-->", i, end = " ")

print("\nTotal head movement: ", head_move)


fcfs_unordered(processes, head)
