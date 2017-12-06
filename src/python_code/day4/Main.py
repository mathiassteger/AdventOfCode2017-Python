import src.python_code.InputHelper as iH
import itertools as it

lines = iH.InputHelper(4).lines()
sum = 0;

for line in lines:
    rslt = max([int(sorted(a) == sorted(b)) for a, b in it.combinations(line.split(" "), 2)])

    if rslt == 0:
        sum+=1
u
print(sum)
