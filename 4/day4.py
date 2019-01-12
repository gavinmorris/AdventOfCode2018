import re

def getInfo(stri):
    #hours + minutes
    pattern = '\d{1,2}:\d{1,2}'
    match = re.search(pattern, stri)
    hour = match.group(0)

    regexp = re.compile(r'#(\d+)')

    #get Id
    if(regexp.search(stri)):
        patternID = '#(\d+)'
        Id = re.search(patternID, stri)
        print Id.group(0)
    print hour


with open("input.txt") as fp:
    values = {}
    for line in fp:
        getInfo(line.strip())

