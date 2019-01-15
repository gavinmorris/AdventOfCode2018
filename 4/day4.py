import re

def wrtd2(s):
    return max(list(s.items()), key=lambda x: sum(x[1]))[0]

with open("input.txt") as fp:
    values = {}
    sleep ={}
    guard_id = None
    time = None
    hoursSleep = None
    for line in fp:
        stri = line.strip()
        regexp = re.compile(r'#(\d+)')
        timeregexp = re.compile(r'(\d{1,2}):(\d{1,2})')
        #if there is an id
        if regexp.search(stri):
            patternTime = '(\d{1,2}):(\d{1,2})'
            hoursSleep = []
            time = re.search(patternTime, stri)
            patternID = '#(\d+)'
            guard_id = re.search(patternID, stri)
            values[guard_id.group()] = time
            if guard_id.group() not in sleep:
                sleep[guard_id.group()] = 0

        elif 'falls asleep' in stri:
            #hours + minutes
            patternTime = '(\d{1,2}):(\d{1,2})'
            time = re.search(patternTime, stri)
            values[guard_id.group()] = time
        elif 'wakes up' in stri:
            #hours + minutes
            patternTime = '(\d{1,2}):(\d{1,2})'
            time = re.search(patternTime, stri)
            mins = int(time.groups(1)[1])
            hour = int(values[guard_id.group()].groups(1)[0])
            if hour == 23:
                hoursSleep.append(mins - (60 - int(values[guard_id.group()].groups(1)[1])))
            else:   
                hoursSleep.append(mins - int(values[guard_id.group()].groups(1)[1]))
            values[guard_id.group()] = time
        
        if guard_id.group() not in sleep:
            sleep[guard_id.group()] = hoursSleep
        elif not sleep[guard_id.group()]:
            sleep[guard_id.group()] = hoursSleep
        elif not hoursSleep:
            pass
        else:
            if sum(sleep[guard_id.group()]) < sum(hoursSleep):
                sleep[guard_id.group()] = hoursSleep

printwrtd2(sleep)

print sleep