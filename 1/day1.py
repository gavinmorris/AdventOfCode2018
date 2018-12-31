#! /usr/bin/python3

def whatIsFrequency(filepath, frequency):
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            newValue = int(line)
            frequency = changeFrequency(newValue, frequency)
            line = fp.readline()
    fp.close()
    return frequency


def changeFrequency(newValue, currFrequency):
    newFrequency = currFrequency + newValue
    print(frequencyChangeMessage(newValue, currFrequency, newFrequency))
    return newFrequency

def frequencyChangeMessage(currFrequency, newValue, newFrequency):
    return "Current frequency  "+str(currFrequency)+", change of "+str(newValue)+"; resulting frequency " + str(newFrequency) +"."


print(whatIsFrequency("./input.txt", 0))
