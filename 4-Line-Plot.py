import matplotlib.pyplot as plt

with open("Goals.txt", "r") as goalData:
    homeTeamLine = goalData.readline()
    homeTeamLine = homeTeamLine.strip(" \n")
    homeTeamLine = homeTeamLine.split(" ")
    
    HomeTeamGoals = [int(x) for x in homeTeamLine]
    
    awayTeamLine = goalData.readline()
    awayTeamLine = awayTeamLine.strip(" \n")
    awayTeamLine = awayTeamLine.split(" ")
    
    AwayTeamGoals = [int(x) for x in awayTeamLine]


x = []
for i in range(1, len(HomeTeamGoals)+1):
    x.append(i)
    
# print(x)

fig2 = plt.figure("Second",figsize=(10,10))
ax1 = fig2.add_subplot(1,1,1)
# ax1.plot(x, HomeTeamGoals, color = "#0F0F0F")
# ax1.plot(
#     x,
#     HomeTeamGoals, 
#     color = (1,0,.5), 
#     marker = "^", 
#     markerfacecolor = "blue",
#     markersize = 8,
#     linestyle = "--",
#     linewidth=1
#     )

# ax1.plot(
#     x,
#     AwayTeamGoals, 
#     color = "green", 
#     marker = "*", 
#     markerfacecolor = "black",
#     markersize = 8,
#     linestyle = ":",
#     linewidth=1
#     )

# ax1.scatter(
#     x,
#     AwayTeamGoals, 
#     color = "orange"
#     )

ax1.plot(
    x,
    HomeTeamGoals, 
    color = (1,0,.5), 
    linestyle = "--",
    linewidth=1
    )

ax1.plot(
    x,
    AwayTeamGoals, 
    color = "green", 
    linestyle = ":",
    linewidth=1
    )

# ax1.scatter(
#     x,
#     AwayTeamGoals, 
#     color = "orange"
#     )

plt.show()
    