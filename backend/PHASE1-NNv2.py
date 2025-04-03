
## temp text
#funcs in upper-starting camelm vars in lower-starting camel

#imports

import random


#vars

width = 2
dimensions = 2
layerCount = 1
weightLayers = []


#funcs

def RecusiveWeightLayersConstruction(mat, dim):

    dim -= 1

    mat.append()

    if dim > 0:

        for i in range(width):

            mat.append(RecusiveWeightLayersConstruction([],dim))
            
    else:

        return random.random


def WeightLayersConstruction():

    for i in range(layerCount):

        weightLayers.append(RecusiveWeightLayersConstruction([],dimensions))

def ActivationFunc(input):
    if input >= 0:
        return 1
    else:
        return 0

def MatMul_Activation(X, Y):

    Z = []

    for a in range(len(X)):
        Z.append([])


    for a in range(len(X)):
        for b in range(len(Y[0])):
            sum = 0
            for i in range(len(Y)):
                sum += X[a][i] * Y[i][b]

            Z[a].append(ActivationFunc(sum))

    return Z

def Computation(input):
    
    currentInput = input

    for i in range(len(weightLayers)):
        currentInput = MatMul_Activation(currentInput, weightLayers[i])

    # fix this please ftlog

    sum = 0

    for i in range(len(currentInput)):
        for j in range(len(currentInput[0])):
            sum += currentInput[i][j]

    return sum

'''
#cool but useless
def FindMatrixDimention(matrix):
    count = 0
    while (type(matrix) == list) and (len(matrix) > 0):
        if len(matrix) > 1:
            count += 1
        matrix = matrix[0]
    return count
#'''

# main prog

inputVector = [[1,1]]

WeightLayersConstruction()

print(weightLayers)

#print(Computation(inputVector))




# need to add cost func (ie a func that you wish the nn to imitate and then make a cost func, and for now just implement random changes and 
# iterate and check to see if better than current until it becomes best possible)