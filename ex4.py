user_num = int(input('Digit a number: '))

if user_num % 3 == 0 and user_num % 5 == 0 :
    print('FizzBuzz')
    
else:
    print(f"{user_num}")