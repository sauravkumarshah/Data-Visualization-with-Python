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


fig = plt.figure("MyFirstFigure",figsize=(10,6)) #(width, height)
fig2 = plt.figure("Second",figsize=(10,10), facecolor="red")

# ax1 = fig2.add_subplot(3,3,2) #nrows,ncolumns,index such that 1<=index<=nrows*ncolumns
# ax3 = fig2.add_subplot(3,1,3)
# ax2 = fig2.add_subplot(3,1,2)
#ax4 = fig2.add_subplot(3,1,5) #ValueError: num must be an integer with 1 <= num <= 3, not 4

axList = []

for i in range(1,10):
    axList.append(fig2.add_subplot(3,3,i))
    
    # plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.1)
    
# axList[0].scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.1)


plt.sca(axList[3])
plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.1)

plt.sca(axList[8])
# plt.scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.9)
axList[6].scatter(HomeTeamGoals, AwayTeamGoals, s = 70, c="#0F0F0F", marker="*", alpha=0.9)

plt.show()
    