def fifo_page_replacement(reference_string, capacity):
    frames = []
    page_faults = 0
    page_hits = 0

    for page in reference_string:
        if page in frames:
            page_hits += 1
        else:
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

    total_requests = len(reference_string)
    hit_ratio = page_hits / total_requests

    print("No of Page Hits:", page_hits)
    print("No of Page Faults:", page_faults)
    print(f"Page Hit Ratio: {hit_ratio:.2f} ({hit_ratio * 100:.2f}%)")


reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 3

fifo_page_replacement(reference_string, frame_size)