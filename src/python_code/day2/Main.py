import src.python_code.InputHelper as iH

iH = iH.InputHelper(2)
lines = iH.lines()
sum = 0

for line in lines:
    numbers = [int(x) for x in line.split('\t')]

    rslt1 = [int(y/x) for x in numbers for y in numbers if y%x == 0]
    sum += max(rslt1)

print(sum)

#ez oneliner:
#print(sum([(max([int(y/x) for x in [int(x) for x in line.split('\t')] for y in [int(x) for x in line.split('\t')] if y%x == 0])) for line in lines]))

