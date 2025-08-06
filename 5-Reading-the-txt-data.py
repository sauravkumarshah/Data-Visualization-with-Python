def readTxt():
    f = open("Sheet1E1.txt","r")
    data = {}
    
    for line in f:
        part1 = line.strip("\n").split(" ")
        dataName = part1[0]
        restData = part1[1:]

        finalData = []
        for x in restData:
            finalData.append(int(x))
            
            data[dataName] = finalData
        
    return data

txtVersionData = readTxt()
# print(txtVersionData.keys())

print(txtVersionData["Games"][0:5])

        