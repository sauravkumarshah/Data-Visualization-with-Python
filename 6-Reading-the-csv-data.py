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
        
    f.close()
        
    return data

def readCSV():
     f = open("Sheet1E1.csv","r")
     data = {}
     
     firstLine = f.readline().strip("\n").split(",")[1:]
     for name in firstLine:
         data[name] = []
         
     for line in f:
         processedLine = line.strip("\n").split(",")[1:]
         # print(processedLine)
         # indexCounter = 0
         # for name in firstLine:
         #     data[name].append(int(processedLine[indexCounter]))
         #     indexCounter += 1
         
         for index in range(len(processedLine)):
             name = firstLine[index]
             dataPoint = int(processedLine[index])
             data[name].append(dataPoint)
     
     return data

    

     
# txtVersionData = readTxt()
csvVersionData = readCSV()
print(csvVersionData["Games"][:5])
        