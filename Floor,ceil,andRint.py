import numpy as np
l=list(map(float,input().split()))
arr=np.array(l)
np.set_printoptions(sign=" ")
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


