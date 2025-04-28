
import random
import numpy


## Base class for all iterated objects (basically everything in NN)


class iteratorClass:
    

    def __init__(self):
        pass
    

    def function(self, currentElement1, currentElement2, indexes1, indexes2, indexesOutput): # blank function including indexes to be overwritten
        return self.subFunction(currentElement1, currentElement2)
    
    
    def subFunction(self, a, b): # blank subfunction just in terms of elements to be overwritten
        return a
    
    
    def constructor(self, list, widths):

        if len(widths) > 0:

            for i in range(widths[0]):
                list.append(0.0)
                list[i] = self.constructor([], widths[1:])

            return list

        else: return 0.0
    
    
    def multiloop(self, input1, input2, output, totalWidths, input1Order, input2Order, cancelledNum, total):

        numpyOutput = numpy.array(output) # make numpy array of output array to link the elements to the original list

        for t in range(total): # have single index to derive all others from

            currentElement1 = input1 # current "layer" of base input
            currentElement2 = input2 # current "layer" of second input
            currentElementOutput = numpyOutput # current "layer" of output
            indexes1 = [] # array of input1's index values
            indexes2 = [] # array of input2's index values
            indexesOutput = [] # array of output's index values
            
            base = 1/totalWidths[-1] # divide to counter fact that initially num = 0 meaning that when going through following loop b will be 1 in the calc 

            for (num, value) in enumerate(totalWidths):

                base *= totalWidths[num-1] # "base" of the specific index, basically how many loops before index increments
                index = int(t/base) - ( value * int( t/(value * base) ) ) # "generalised" form of the (in this case) (num+1)th digit of a number equation, where each digit can have a different "base"

                if num < input1Order: # only is in terms of first "input1Order" indexes
                    indexes1.append(index)
                    currentElement1 = currentElement1[index] # move down one "layer" in the base input
                
                if num + 1 > input1Order - cancelledNum: # only in terms of trailing indexes bar those that input1 doesnt cancel with input2 (+1 due to indexing 0)
                    indexes2.append(index)
                    currentElement2 = currentElement2[index] # move down one "layer" in the second input

                if num + 1 < input1Order + input2Order - (2 * cancelledNum): #need array containing var to change so that can change output via linked slice
                    indexesOutput.append(index)
                    currentElementOutput = currentElementOutput[index] # move down one "layer" in the output
            
            if type(currentElementOutput.tolist()) == list:
                currentElementOutput[index] = self.function(currentElement1, currentElement2, indexes1, indexes2, indexesOutput )
            else:
                currentElementOutput = self.function(currentElement1, currentElement2, indexes1, indexes2, indexesOutput )

            #print(currentElementOutput)

        output = numpyOutput.tolist()
        return output
    

    def WidthCalc(self, input1, input2, outputOrder):

        # pre-emptive definitions

        total = 1 # total number of loops that must occur to iterate through every unique index value
        widthInput1 = input1 # term used to calculate dimensions of first input
        widthInput2 = input2 # term used to calculate dimensions of second input
        input1Widths = [] # array of widths of the first input of each index in order
        input2Widths = [] # array of widths of the second input of each index in order
        outputWidths = [] # array of widths of the output of each index in order
        widthCheck = 0 # check to flag if widthhs of inputs are different
        cancelledNumCheck = 0 # check to flag if widthhs of inputs are different

        # first widths

        while type(widthInput1) is list: # while loop is not great
            input1Widths.append(len(widthInput1))
            total *= len(widthInput1)
            widthInput1 = widthInput1[0] # move down 1 layer in first input

        while type(widthInput2) is list:
            input2Widths.append(len(widthInput2))
            total *= len(widthInput2)
            widthInput2 = widthInput2[0] # move down 1 layer in second input

        cancelledNum = (len(input1Widths) + len(input2Widths) - outputOrder) / 2 # number of pairs of indexes being cancelled in pseudo-application

        # error checking

        if int(cancelledNum) < 0:
            print("IMPOSSIBLE OUTPUT ORDER ERROR - TOO HIGH")
            cancelledNumCheck += 1

        if int(cancelledNum) > len(input2Widths):
            print("IMPOSSIBLE OUTPUT ORDER ERROR - TOO MANY")
            cancelledNumCheck += 1

        if int(cancelledNum) != int(cancelledNum + 0.5):
            print("IMPOSSIBLE OUTPUT ORDER ERROR - ODD CANCELLEDNUM")
            cancelledNumCheck += 1
        
        if cancelledNumCheck > 0:
            cancelledNum = 0 # default to 0 as cannot result in error as is just ptensor prod

        cancelledNum = int(cancelledNum) # make int for calls later

        for i in range(cancelledNum):
            widthCheck += (input1Widths[i + (len(input1Widths) -1 -cancelledNum)] - input2Widths[i])**2 # square to get absolute error, where the inner indexes are cancelled
            total /= input2Widths[i] # remove duplicate iterations through such indexes from total
            total = int(total) # make int for calls later
        
        if widthCheck > 0:
            print("WIDTH MISMATCH ERROR")
            cancelledNum = 0

        # rest of widths

        outputWidths = input1Widths[:len(input1Widths) - cancelledNum] + input2Widths[cancelledNum:]
        totalWidths = input1Widths + input2Widths[cancelledNum:] # array of all iterated widths

        return input1Widths, input2Widths, outputWidths, totalWidths, cancelledNum, total
        
        
    def PtensorCalc(self, input1, input2, outputOrder): # input tensors, output tensor + desired order of output tensor, function deteminining term-by term calc

        input1Widths, input2Widths, outputWidths, totalWidths, cancelledNum, total = self.WidthCalc(input1, input2, outputOrder) # calculate widths of dimensions + number of cancelled indexes/dimensions

        output = self.constructor([], outputWidths) # create empty output to be overwritten

        return self.multiloop(input1, input2, output, totalWidths, len(input1Widths), len(input2Widths), cancelledNum, total)


## Child classes

class randomClass(iteratorClass): # initial weights, inherit from iterator

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return a + random.random() - 0.5 # initially random


class ptensorApplicationClass(iteratorClass): # application of ptensors, for weight layers

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return a * b # ptensor application


class activationFuncClass(iteratorClass): # application of activation func (same for each layer FOR NOW)

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return 1/( 1 + (2**-a) ) # sigmoid func
    

class activationFuncDerivativeClass(activationFuncClass): # derivative of activation func for backprop

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def function(self, currentElement1, currentElement2, indexes1, indexes2, indexesOutput): # overite of function
        h = 2**(-4) # infinitesimal approx
        return (self.subFunction(currentElement1 + h, currentElement2) - self.subFunction(currentElement1, currentElement2) ) / h # first principles derivative


class targetFuncClass(iteratorClass): # target function to be replicating

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return a + 1 # simple FOR NOW  


class costFuncClass(iteratorClass): # target function to be replicating

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return (a - b)**2 # square to get absolute difference



## Mainprog

layerCount = 2
trainingCycles = 2
width = 10
mainIterator = iteratorClass()
randomiser = randomClass()
applier = ptensorApplicationClass()
activationFunc = activationFuncClass()
costFunc = costFuncClass()
targetFunc = targetFuncClass()

emptyWeights = [ mainIterator.constructor([], [width, width, width, width]) for i in range(layerCount) ]
weights = [ randomiser.PtensorCalc(emptyWeights[i], None, 4) for i in range(layerCount) ]

for i in range(trainingCycles):
    
    emptyInput = mainIterator.constructor([], [width, width])
    currentInput = randomiser.PtensorCalc(emptyInput, None, 2)
    targetOutput = targetFunc.PtensorCalc(currentInput, None, 2)

    for j in range(layerCount):

        currentInput = applier.PtensorCalc(weights[j], currentInput, 2)
        currentInput = activationFunc.PtensorCalc(currentInput, None, 2)

    cost = costFunc.PtensorCalc(currentInput, targetOutput, 0)

    print(cost)



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