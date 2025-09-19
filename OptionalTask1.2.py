#Modify code so that it prints numbers on each line for the sample.txt file

with open('sample.txt', 'r') as f:
    lines = f.readlines()

with open('sample.txt', 'w') as f:
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}")
