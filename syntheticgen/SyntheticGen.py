import random
import numpy as np

def remove_from_array(base_array, test_array):
    for index in range(len(base_array)):
        if np.array_equal(base_array[index], test_array):
            base_array.pop(index)
            break

class linearAugmentor:

	baseSet = []
	operationRange = [1,100]
	matrix = []

	def __init__(self, dataset):
		self.dataset = dataset
		for each in dataset:
			self.baseSet.append(each)

	def addMatrix(self, percentAdded):

		numLeft = len(self.dataset) - (len(self.dataset) * percentAdded)

		starting = self.dataset

		if percentAdded == 1.0:
			self.matrix = dataset

		else:
			while len(starting) > numLeft:
				row = starting[random.randint(0,len(starting)-1)]
				self.matrix.append(row)
				remove_from_array(starting, row)


	def setIntRange(self, lowerBound, upperBound):
		self.operationRange[0] = lowerBound
		self.operationRange[1] = upperBound

	def setPowerRange(self, lowerBound, upperBound):
		self.operationRange[0] = int(len(self.matrix) ** lowerBound)
		self.operationRange[1] = int(len(self.matrix) ** upperBound)

	def performOperations(self):
		numOperations = random.randint(self.operationRange[0], self.operationRange[1])

		while numOperations > 0:

			operation = random.randint(0, 1)

			row1Num = random.randint(0, len(self.matrix)-1)
			row2Num = random.randint(0, len(self.matrix)-1)

			while row1Num == row2Num:
				row2Num = random.randint(0, len(self.matrix)-1)

			row1 = self.matrix[row1Num]
			row2 = self.matrix[row2Num]

			row1List = []
			for data in row1:
				row1List.append(data)

			row2List = []
			for data in row2:
				row2List.append(data)

			multiple = random.randint(1,9)
			operator = random.randint(0,1)

			if operation == 0:
				for i in range(0, len(row1List)):
					if operator == 0:
						row1List[i] = row1List[i] - multiple * row2List[i]
					else:
						row1List[i] = row1List[i] + multiple * row2List[i]

			else:
				for i in range(0, len(row1List)):
					if operator == 0:
						row1List[i] = row1List[i] * multiple * -1
					else:
						row1List[i] = row1List[i] * multiple

			row1List[len(row1List)-1] = int(row1List[len(row1List)-1])

			if row1List[len(row1List)-1] > 1:
				row1List[len(row1List)-1] = 1

			if row1List[len(row1List)-1] < 0:
				row1List[len(row1List)-1] = 0

			newRow1 = np.array(row1List)

			remove_from_array(self.matrix, row1)

			self.matrix.insert(random.randint(0, len(self.matrix)-1),newRow1)



			numOperations = numOperations - 1

	
	def getCombinedSet(self):
		newSet = []
		for each in self.baseSet:
			newSet.append(each)
		for each in self.matrix:
			newSet.append(each)

		random.shuffle(newSet)
		print(newSet)
		return newSet

	def getSyntheticData(self):
		return self.matrix

	def getInitialDataset(self):
		return self.baseSet


#class imageAugmentor:









