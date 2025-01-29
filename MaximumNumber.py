num = (32,2423,4345,34534,2,43)

maxNumber = num[0]

for i in range(1,len(num)):
  if(num[i] > maxNumber):
    maxNumber = num[i]

print("Maximum Number : " , maxNumber)