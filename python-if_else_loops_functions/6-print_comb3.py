#!/usr/bin/python3
for t in range(10):
    for u in range(t, 10):
        if t != u:
            print(f"{t}{u}", end=", " if t != 8 or u != 9 else "")
print()  # Add a new line at the end
