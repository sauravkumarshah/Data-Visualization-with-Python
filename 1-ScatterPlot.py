import matplotlib.pyplot as plt
import math

with open("Goals.txt", "r") as goalData:
    homeTeamLine = goalData.readline()
    homeTeamLine = homeTeamLine.strip(" \n")
    homeTeamLine = homeTeamLine.split(" ")
    
    HomeTeamGoals = [int(x) for x in homeTeamLine]
    
    awayTeamLine = goalData.readline()
    awayTeamLine = awayTeamLine.strip(" \n")
    awayTeamLine = awayTeamLine.split(" ")
    
    AwayTeamGoals = [int(x) for x in awayTeamLine]
    
print(HomeTeamGoals)
print(AwayTeamGoals)

#plt.scatter(x = HomeTeamGoals, y = AwayTeamGoals)
#plt.scatter(HomeTeamGoals, AwayTeamGoals)
#plt.scatter(y = HomeTeamGoals, x = AwayTeamGoals)
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="c")
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F")
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=[[1,0,1]])
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=[[1,0,.4,.9]])
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c='red')
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=HomeTeamGoals)
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=AwayTeamGoals)
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=range(len(AwayTeamGoals)))

def distFromZero(htg, atg):
    return math.sqrt(htg**2 + atg**2)

colors = []

for i in range(len(HomeTeamGoals)):
    colors.append(distFromZero(HomeTeamGoals[i], AwayTeamGoals[i]))
    
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=colors)
#plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=colors, marker='^')
plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c=colors, marker='^', alpha=0.3)

plt.show()
    
    