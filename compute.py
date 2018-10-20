import math 
import iris as ir

k = 3

testD = {}

def compute(v1,v2,v3,v4):
	dist = []
	global testD
	testD = {
		0:{
		'sepalLength':v1,
		'sepalWidth':v2,
		'petalLength':v3,
		'petalWidth':v4
		}
	}	
	noOfValues=len(ir.trainD)
	for i in range(noOfValues):
		tmp=math.sqrt(((ir.trainD[i]['sepalLength']-testD[0]['sepalLength'])**2) + ((ir.trainD[i]['sepalWidth']-testD[0]['sepalWidth'])**2) + ((ir.trainD[i]['petalLength']-testD[0]['petalLength'])**2) + ((ir.trainD[i]['petalWidth']-testD[0]['petalWidth'])**2))
		dist.append(round(tmp,3))

	#print(dist)
	kNeighbours = []

	for i in range(k):
		n = min(dist)
		v = dist.index(n)
		dist.remove(n)
		dist.insert(v,9999)
		kNeighbours.append(v)
		#print(dist)

	#print(kNeighbours)

	classes = []
	for i in kNeighbours:
		classes.append(ir.trainD[i]['species'])

	#print(classes)
	classCount = {'setosa':0,'versicolor':0,'virginica':0}
	for i in classes:
		classCount[i] += 1

	maxsp = 'setosa'
	if(classCount['versicolor']>classCount[maxsp]):
		maxsp = 'versicolor'
	if(classCount['virginica']>classCount[maxsp]):
		maxsp = 'virginica'

	print(maxsp)
		


