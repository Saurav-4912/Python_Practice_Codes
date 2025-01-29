number = int(input("Enter the number : "))

is_prime = True
for i in range( 2 , number):
  if number % i == 0:
    is_prime = False
    break

if is_prime:
  print(number , "is prime")
else:
  print(number , "is not prime")