import sys

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    print(line)