import src.python_code.InputHelper as iH

iH = iH.InputHelper(1)
lines = iH.lines()

for line in lines:
    line = line.strip()
    sum = 0
    for index, number in enumerate(line):
        sum += int(number) if line[((index+(len(line)//2)) % len(line))] == number else 0
    print(sum)


