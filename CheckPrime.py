def check_prime(number):

  if number < 2:
    return False
  
  for i in range(2,number):
    if number % i == 0:
      return False
    
  return True

number = int(input("Enter the number :"))
if check_prime(number):
  print("Given number is prime number")
else:
  print("Given number is not prime number")