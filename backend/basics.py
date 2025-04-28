
import random



class iterator:
    

    def __init__(self):
        pass
    

    def function(self, currentElement1, currentElement2, indexes1, indexes2, indexesOutput): # blank function including indexes to be overwritten
        result = self.subFunction(self, currentElement1, currentElement2)
        return result
    
    
    def subFunction(self, a, b): # blank subfunction just in terms of elements to be overwritten
        return a * b
    
    
    def constructor(self, list, widths):

        if len(widths) > 1:

            for i in range(widths[0]):
                list.append([])

            for i in list:
                i = self.constructor(self, i, widths[1:])

            return list

        if len(widths) == 1:

            for i in range(widths[0]):
                list.append(0)
            
            return list

        else: return None
    
    
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
                    currentElement1 = currentElement1[index1] # move down one "layer" in the base input
                
                if num + 1 > input1Order - cancelledNum: # only in terms of trailing indexes bar those that input1 doesnt cancel with input2 (+1 due to indexing 0)
                    indexes2 = index
                    currentElement2 = currentElement2[index2] # move down one "layer" in the second input

                if num + 1 < input1Order + input2Order - cancelledNum: #need array containing var to change so that can change output via linked slice
                    indexesOutput = index
                    currentElementOutput = currentElementOutput[indexOutput] # move down one "layer" in the output

            currentElementOutput[index] = self.function(self, currentElement1, currentElement2, indexes1, indexes2, indexesOutput )
            print(currentElementOutput)

        output = numpyOutput.tolist()
        return output
    

    def WidthCalc(self, input1, input2, outputOrder):

        total = 1 # total number of loops that must occur to iterate through every unique index value
        widthInput1 = input1 # term used to calculate dimensions of first input
        widthInput2 = input2 # term used to calculate dimensions of second input
        input1Widths = [] # array of widths of the first input of each index in order
        input2Widths = [] # array of widths of the second input of each index in order
        outputWidths = [] # array of widths of the output of each index in order
        check = 0 # check to flag if widthhs of inputs are different

        while type(widthInput1) is list: # while loop is not great
            input1Widths.append(len(widthInput1))
            total *= len(widthInput1)
            widthInput1 = widthInput1[0] # move down 1 layer in first input

        while type(widthInput2) is list:
            input2Widths.append(len(widthInput2))
            total *= len(widthInput2)
            widthInput2 = widthInput2[0] # move down 1 layer in second input

        cancelledNum = (len(input1Widths) + len(input2Widths) - outputOrder) / 2 # number of pairs of indexes being cancelled in pseudo-application
        cancelledNum = int(cancelledNum) # make int

        for i in range(cancelledNum):
            check += (input1Widths[i + (len(input1Widths) -1 -cancelledNum)] - input2Widths[i])**2 # square to get absolute error, where the inner indexes are cancelled
            total /= input2Widths[i] # remove duplicate iterations through such indexes from total

        if check > 0: print("WIDTH MISMATCH ERROR")

        outputWidths = input1Widths[:len(input1Widths) - cancelledNum] + input2Widths[cancelledNum:]
        totalWidths = input1Widths + input2Widths[cancelledNum:] # array of all iterated widths

        return input1Widths, input2Widths, outputWidths, totalWidths, cancelledNum, total
        
        
    def PtensorCalc(self, input1, input2, outputOrder): # input tensors, output tensor + desired order of output tensor, function deteminining term-by term calc

        input1Widths, input2Widths, outputWidths, totalWidths, cancelledNum, total = self.WidthCalc(self, input1, input2, outputOrder) # calculate widths of dimensions + number of cancelled indexes/dimensions

        output = self.constructor([], outputWidths) # create empty output to be overwritten

        return self.multiloop(self, input1, input2, output, totalWidths, len(input1Widths), len(input2Widths), cancelledNum, total)




class initialWeights(iterator): # foo is an iterator

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def subFunction(self, a, b): # overite of function
        return a + random.random() - 0.5



X = initialWeights.constructor(initialWeights, [], [3,3,3])
print(X)
initialWeights.PtensorCalc(self, X, None, [3,3,3])

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