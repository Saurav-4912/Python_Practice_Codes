number = int(input("Enter the number : "))

a=0
b=1
for i in range(1,number+1):
  print(a,end=" ")
  temp = a + b
  a=b
  b=temp