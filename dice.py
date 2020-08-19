import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
count=[]
diceResult=[]
for  i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)
#print(count,diceResult)
mean=sum(diceResult)/len(diceResult)
print(mean)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)
print(median)
print(mode)
standardDeviation=statistics.stdev(diceResult)
print(standardDeviation)
firstStandardDeviationStart,firstStandardDeviationEnd=mean-standardDeviation,mean+standardDeviation
secondStandardDeviationStart,secondStandardDeviationEnd=mean-(2*standardDeviation),mean+(2*standardDeviation)
thirdStandardDeviationStart,thirdStandardDeviationEnd=mean-(3*standardDeviation),mean+(3*standardDeviation)
listOfDataWithinFirstStandardDeviation=[result for result in diceResult if result>firstStandardDeviationStart and result<firstStandardDeviationEnd]
listOfDataWithinSecondStandardDeviation=[result for result in diceResult if result>secondStandardDeviationStart and result<secondStandardDeviationEnd]
listOfDataWithinThirdStandardDeviation=[result for result in diceResult if result>thirdStandardDeviationStart and result<thirdStandardDeviationEnd]

print("{}% of data lies within first standardDeviation".format(len(listOfDataWithinFirstStandardDeviation)*100.0/len(diceResult)))
print("{}% of data lies within second standardDeviation".format(len(listOfDataWithinSecondStandardDeviation)*100.0/len(diceResult)))
print("{}% of data lies within third standardDeviation".format(len(listOfDataWithinThirdStandardDeviation)*100.0/len(diceResult)))
#fig=px.bar(x=diceResult,y=count)
#fig.show()
#fig=ff.create_distplot([diceResult],['result'])
#fig.show()