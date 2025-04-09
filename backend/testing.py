def DeepCopy(A, B): #copy B into A without linking - can prob find a better method to this
    A.clear()
    A.extend(B)

Y = [1,2,3]
X = []
DeepCopy(X, Y)
Y = [5]

print(X, Y)