
def mru_page_replacement(pages, frame_size):
    frames = []
    last_used = {}
    page_faults = 0
    page_hits = 0

    print("\nPage\tFrames\t\tStatus")

    for time, page in enumerate(pages):
        if page in frames:
            page_hits += 1
            status = "HIT"
        else:
            page_faults += 1

            if len(frames) < frame_size:
                frames.append(page)
            else:
                mru_page = max(frames, key=lambda p: last_used[p])
                frames[frames.index(mru_page)] = page

            status = "FAULT"

        last_used[page] = time

        print(f"{page}\t{frames}\t\t{status}")

    print("\nTotal Page Faults:", page_faults)
    print("Total Page Hits:", page_hits)


pages = list(map(int, input("Enter reference string: ").split()))
frame_size = int(input("Enter frame size: "))

mru_page_replacement(pages, frame_size)
