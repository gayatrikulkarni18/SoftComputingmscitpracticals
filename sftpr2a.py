import numpy as np 
print("ANDNOT function using MP\n")
x1inputs = [1,1,0,0]
x2inputs = [1,0,1,0]

print("Considering all weights as excitatory");
w1 = [1,1,1,1]
w2 = [1,1,1,1]

yin = []
print("x1","x2","yin")
for i in range(0,4):
  yin.append(x1inputs[i]*w1[i] + x2inputs[i]*w2[i])
  print(x1inputs[i]," ",x2inputs[i]," ", yin[i])


print("Considering all weights as excitatory");
w1 = [1,1,1,1]
w2 = [-1,-1,-1,-1]

yin = []
print("x1","x2","yin")
for i in range(0,4):
  yin.append(x1inputs[i]*w1[i] + x2inputs[i]*w2[i])
  print(x1inputs[i]," ",x2inputs[i]," ", yin[i])

theta = 2*1-1
print("Threshold -Theta =",theta)
print("Applying Threshold ")
y = []
for i in range(0,4):
  if(yin[i]>=theta):
    value = 1
    y.append(value)
  else:
    value = 0
    y.append(value)
print("x1","x2","y")


for i in range(0,4):
  print(x1inputs[i]," ",x2inputs[i]," ",y[i])

