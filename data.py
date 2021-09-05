import csv
#counter is a prdefined class
from collections import Counter

with open("mmm/data.csv", newline="") as f:
    reader = csv.reader(f) 
    fileData = list(reader)
    fileData.pop(0)
    
    
print(fileData[1][1])

weightList=[]
for i in range(0, len(fileData)):
    weight = fileData[i][1]
    weightList.append(weight)
    
#print(weightList)

sum = 0
for i in range(0, len(weightList)):
    weightList[i]
    sum = sum+float(weightList[i])

mean = sum/len(weightList)

print(mean)
    
#print(sum)

    #float is a decimal

#CALCULATING MEDIAN

weightList.sort()

n = len(weightList)

if len(weightList) %2 == 0:
    median1 = float(weightList[n//2])
    median2 = float(weightList[n//2-1])
    median = (median1 + median2)/2

    
else:
    median = float(weightList[n//2])

#print(weightList)
#floor division is used to divide the number and rounds it to the nearest whole number    

#Mode calculations

#newWeights is our dictionary]
#items() gets us all the key values
newWeights = Counter(weightList)

print(newWeights)

modeDataForRange = {'50-60': 0, '60-70': 0, '70-80': 0 }
for weight, occurance in newWeights.items():
    if float(weight) >50 and float(weight) <60:
        #whatever weight comes between this key, it'll get added
        #to the range+occurance
        modeDataForRange['50-60'] += occurance
    
    elif float(weight) >60 and float(weight) <70:
        modeDataForRange['60-70'] += occurance

    elif float(weight) >70 and float(weight) <80:
        modeDataForRange['70-80'] += occurance

    #pass means that it'll go as it is
    else: pass

    
print(modeDataForRange)

modeRange = 0
modeOccurance = 0

for range, occurance in modeDataForRange.items():
    if occurance> modeOccurance:
        modeRange, modeOccurance = [range.split("-")[0], range.split("-")[1]], occurance
        
    
print(modeRange)

mode = (int(modeRange[0])+int(modeRange[1]))/2

print(mode)


        
