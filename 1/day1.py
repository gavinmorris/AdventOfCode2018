#! /usr/bin/python3

frequencies = []
with open( "./input.txt") as fp:
    line = fp.readline()
    while line:
        frequencies.append(int(line.strip()))
        line = fp.readline()
fp.close()
print(sum(frequencies))

freqSet = set()
curr = frequencies[0]
i = 0
#keep looping until a vlaue is found the set
while curr not in freqSet:
    freqSet.add(curr)
    if i == len(frequencies) - 1: 
        i = 0
    else:
        i+=1
    curr += frequencies[i]

print(curr)