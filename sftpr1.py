inputs = float(input("Enter the input :"))
weights = float(input("Enter the weight :"))
bias = float(input("Enter bias :"))

yin = bias + (inputs * weights)

if yin < 0:
  out = 0
elif yin > 1:
  out= 1
else:
    out = yin
print("Output is :",out)
print('Gayatri Kulkarni -53004230002')
