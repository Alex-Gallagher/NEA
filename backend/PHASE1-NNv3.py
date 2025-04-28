
## temp text
#funcs in upper-starting camelm vars in lower-starting camel

#imports

import random


#vars

width = 2
dimensions = 2
layerCount = 2

weightLayersMatrix = [ [ [
(random.random() - 0.5) for k in range(width)
] for j in range(width)
] for i in range(layerCount)
] # weightLayers[i][j][k] for each element, a list of j by k matrices. thus the index of the matrix is reading the iteration loops upwards


#funcs

def TrainingFunction(X):

    total = 0

    for (i, dummy2) in enumerate(X):

        for (j, dummy3) in enumerate(X[0]):
        
            total += X[i][j]

    output = [ [
    total for (j, dummy1) in enumerate(X[0])
    ] for (i, dummy2) in enumerate(X)
    ]

    return output

def Costfunction(observedMatrix, expectedMatrix):

    costVar = 1

    cost = 0

    if len(observedMatrix) == len(expectedMatrix) and len(observedMatrix[0]) == len(expectedMatrix[0]):
            
        for (i, dummy1) in enumerate(expectedMatrix):
        
            for (j, dummy2) in enumerate(expectedMatrix[0]):

                cost += costVar * (expectedMatrix[i][j] - observedMatrix[i][j])**2

    else:

        print("OUTPUT WIDTH DISPARITY ERROR")

        print("OBSERVED;", observedMatrix)

        print("EXPECTED;", expectedMatrix)

        print("-----------------------")
    
    return cost





def WeightLayersFunction(i=-1, j=-1, k=-1): # encode matrix as a function, where default arguements behave as matrix does
    if i == -1:
        return weightLayersMatrix
    elif j == -1:
        return weightLayersMatrix[i]
    elif k == -1:
        return weightLayersMatrix[i][j]
    else:
        return weightLayersMatrix[i][j][k]

def ActivationFunc(input): #sigmoid
    if input >= 1000:
        result = 1
    elif input <= -1000:
        result = 0
    else:
        result = (1 + (2**(-input)) )**(-1)
    return result

def MatMul_Activation(X, Y): 

    Z = [ [
    0 for (j, dummy1) in enumerate(Y[0])
    ] for (i, dummy2) in enumerate(X)
    ] # i use enumerate here so that range(len()) is not required

    if len(X[0]) == len(Y):
            
        for (i, dummy1) in enumerate(X):
        
            for (j, dummy2) in enumerate(Y[0]):

                for (k, dummy3) in enumerate(Y):
                
                    Z[i][j] += X[i][k] * Y[k][j]
                
                Z[i][j] = ActivationFunc(Z[i][j])

    else:

        print("MULT WIDTH DISPARITY ERROR")

        print("LEFT;", X)

        print("RIGHT;", Y)

        print("-----------------------")

    return Z

def Computation(weightLayers, input):
    
    currentInput = input

    for (k,dummy1) in enumerate(weightLayers):
        currentInput = MatMul_Activation(weightLayers[k], currentInput)

    # fix this please ftlog

    return currentInput


def CostCalc(weightLayers, input):
    return Costfunction(Computation(weightLayers,input), TrainingFunction(input))


# main prog

inputMatrix = [
[ 1
] for i in range(width)
] # i by 1 matrix (vector)

minCost = 0.1
prevCost = 0
newCost = 9999
prevweightLayersMatrix = []

while CostCalc(WeightLayersFunction(),inputMatrix) > minCost:

    prevCost = newCost

    prevweightLayersMatrix.clear()
    prevweightLayersMatrix.extend(weightLayersMatrix)

            
    for (i, dummy1) in enumerate(WeightLayersFunction()):
    
        for (j, dummy2) in enumerate(WeightLayersFunction(i)):

            for (k, dummy3) in enumerate(WeightLayersFunction(i,j)):

                weightLayersMatrix[i][j][k] += (0.5*prevCost**2) * random.random() - 0.5
    
    newCost = CostCalc(WeightLayersFunction(),inputMatrix)

    if newCost > prevCost:

        weightLayersMatrix.clear()
        weightLayersMatrix.extend(prevweightLayersMatrix)

        newCost = prevCost

    print(newCost)

print(WeightLayersFunction())


#print(inputMatrix)

#print(TrainingFunction(inputMatrix))

#print(Computation(WeightLayersFunction(),inputMatrix))

#print(CostCalc(WeightLayersFunction(),inputMatrix))


'''

-construct weight layers
-weight layers into a function
-training function from input to output (iterator)
-training function (diff between outputs) (iterator)
-activation function (maybe list of them)
-matmul + activation func (have it inherit) (iterator)
-perform computation
-training method eg backprop or random (iterator)

-parameters

'''