#! /usr/bin/python3
import operator
def part1():
    with open("input.txt", "r") as fp:
        two = 0
        three = 0
        for line in fp:
            value = howManyChars(line.strip()) 
            if value == 3:
                three +=1
            elif value == 2:
                two += 1
            elif value == 5:
                two += 1 
                three += 1
    return three * two


def howManyChars(boxCode):
    boxCodeDict = {}
    for c in boxCode:
        if c not in boxCodeDict:
            boxCodeDict[c] = 1
        else:
            boxCodeDict[c] += 1
    
    if 2 in boxCodeDict.values() and 3 not in boxCodeDict.values():
        return 2
    elif 3 in boxCodeDict.values() and 2 not in boxCodeDict.values():
        return 3
    elif 3 in boxCodeDict.values() and 2 in boxCodeDict.values():
        return 5
    else:
        return 1

def part2():
    codes = []
    with open("input.txt", "r") as fp:
        for line in fp:
            codes.append(line.strip())        

        for fs in codes:
            for ss in codes:
                diff = 0
                for i in range(len(fs)):
                    if fs[i] != ss[i]:
                        diff += 1
                if diff == 1:
                    print fs, ss
                    result = []
                    for j in range(len(fs)):
                        if fs[j] == ss[j]:
                            result.append(fs[j])
                    return "".join(result)
                
              
print part1()
print part2()
