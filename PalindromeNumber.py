def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
   
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    
    if original_num == reversed_num:
        return True
    else:
        return False


num = int(input("Enter the number : "))
if is_palindrome(num):
    print("palindrome")
else:
    print("Not palindrome") 


