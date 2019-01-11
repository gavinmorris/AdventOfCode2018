with open("input.txt", "r") as fp:
    values = {}
    overlapCount = 0
    for line in fp:
        #get border
        splitIt = line.split(" ")
        borders = splitIt[2].split(",")
        b1 = int(borders[0])
        b2 = int(borders[1].split(":")[0])
        
        #get area
        splitIt = line.split(" ")
        areas = splitIt[3].split("x")
        x = int(areas[0])
        y = int(areas[1])

        for i in range(0, x):
            for j in range(0, y):
                coord = (b1+i, b2+j)
                if coord in values:
                    values[coord] += 1
                else:
                    values[coord] = 1
    
        #count how many keys have values 2 or over
    print sum(v >= 2 for v in values.values())

       