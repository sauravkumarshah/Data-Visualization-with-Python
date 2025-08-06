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
    
#fig = plt.figure(1,figsize=(10,6)) #(width, height)
#fig2 = plt.figure(2,figsize=(10,10), facecolor="red")

#plt.figure(1)
#plt.figure(2)

fig = plt.figure("MyFirstFigure",figsize=(10,6)) #(width, height)
fig2 = plt.figure("Second",figsize=(10,10), facecolor="red")

plt.figure("MyFirstFigure")
plt.figure("Second")

plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.1)

plt.show()
    
    