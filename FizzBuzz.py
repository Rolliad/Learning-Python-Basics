#FizzBuzz programming challenge

for num in range(101):

    #Prime Number Check
    if num%2 >= 1 and num%3 >= 1 and num%5 >= 1:
        print("Prime")

    #Divisible by both 3 and 5
    elif num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    
    #Divisible by 5
    elif num%5 == 0:
        print("Buzz")
    
    #Divisible by 3
    elif num%3 == 0:
        print("Fizz")
    
    #Divisible by 2
    else:
        print(num)