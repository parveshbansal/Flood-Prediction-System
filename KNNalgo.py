import csv
import random
import math
def handleDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(2):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
def euclideanDistance(instance1, instance2, length):
        distance = 0
        if(instance1[0]==instance2[0]):
            for x in range(1,length):
                    distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)
trainingSet=[]
testSet=[]
handleDataset(r'C:\Users\DELL\Desktop\pi project\ppp.txt', 1, trainingSet, testSet)
print(trainingSet)
print(testSet)
print ('Train: ' + repr(len(trainingSet)))
print ('Test: ' + repr(len(testSet))
import operator 
def getKNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
            dist = euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
    print(distances)
   # distances.sort(key=operator.itemgetter(1))
    print(len(distances))
    i=0
    length1=len(distances)
    while i<length1:
            if distances[i][1]==0.0:
                    distances.remove (distances[i])
                    length1=length1-1
                    continue
            i=i+1
    print(len(distances))        
    distances.sort(key=operator.itemgetter(1))    
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
import requests
res1=requests.get( 'apitofetchdistance')
val1=res1.json()
res2=requests.get( 'apitofetchflowrate')
val2=res2.json()
val1=dict(val1)
val2=dict(val2)
k=val1["field1"]
k1=val2["field3"]
testInstance=[]
print(k,k1)
testInstance.append(k)
testInstance.append(k1)      
k=3
p=getKNeighbors(trainingSet, testInstance, k)
print(p)
