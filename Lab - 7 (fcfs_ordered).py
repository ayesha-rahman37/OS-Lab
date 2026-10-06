processes = [0, 20, 30, 41, 51, 62, 100]
head = 70 
head_move = 0

def fcfs_ordered(prpcesses, head):
    head_move = 0

    print("Processes: ", head, end = " ")


for i in processes:
    movement = abs(i - head)
    head_move += movement
    head = i
    print("-->", i, end = " ")

print("\nTotal head movement: ", head_move)


fcfs_ordered(processes, head)
