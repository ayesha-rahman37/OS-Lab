def sstf(requests, head):
    total_head_movement = 0
    current_head = head
    remaining_requests = requests.copy()
    
    execution_order = []

    while remaining_requests:
        closest_request = min(remaining_requests, key=lambda x: abs(x - current_head))
        
        distance = abs(closest_request - current_head)
        total_head_movement += distance
        
        execution_order.append(closest_request)
        current_head = closest_request
        remaining_requests.remove(closest_request)

    print("--- SSTF Disk Scheduling ---")
    print(f"Initial Head Position: {head}")
    print("Processing Order:", head, end=" ")
    for req in execution_order:
        print(f"--> {req}", end=" ")
        
    print(f"\nTotal Head Movement (Seek Time): {total_head_movement}")

requests = [60, 20, 100, 10, 15, 22, 42]
head = 50

sstf(requests, head)