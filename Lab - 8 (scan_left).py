processes = [0, 20, 30, 41, 51, 62, 100]
head = 70

def scan_left(processes, head):
    head_move = 0
    current_head = head

    left_side = sorted([p for p in processes if p < current_head], reverse=True)
    right_side = sorted([p for p in processes if p > current_head])

    execution_order = left_side + right_side

    print("\nSCAN(Direction:Left)")
    print("Order of processing:", current_head, end=" ")

    temp_head = current_head
    for p in execution_order:
        movement = abs(p - temp_head)
        head_move += movement
        temp_head = p
        print("-->", p, end=" ")

    print("\nTotal head movement:", head_move)


scan_left(processes, head)
