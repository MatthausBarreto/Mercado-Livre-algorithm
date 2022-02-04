def process(user_number, user_condition):
    length = int(len(user_number))
    number_as_int = int(user_number)
    counter = 0

    for i in range(0, length):      
        
        #checks if the user input number has a digit equal or greater than 7
        if user_condition < 0 or user_condition > 9:
            return print('sorry, invalid input, number must be an integer between 0 and 9.')

        #checks if the the user input fits the number of digits allowed
        elif i > 3:
            return print('sorry, invalid input, type an integer between 0 and 9999.')
        
    #loops through the numbers until the user's input number
    for i in range(0, number_as_int):
        number_as_str = str(i)
        sum = 0
        
        #this gets every digit in the current number and casts it into an integer
        for digit in number_as_str:
            digit = int(digit)
            
            #checks the current digit to either get out of the loop or continue to sum the digits
            if digit >= user_condition:
                break
            
            else: 
                sum += int(digit)        
        
        #checks if the digits sum is equal to 21    
        if sum == 21:
            counter += 1
    
    #final output 
    return print('the total of numbers which it\'s sum was 21:', counter)

#gets the number to be looped through 
user_input = input('Type a number between 0 and 9999:')

#gets the digit condition
user_input_condition = int(input('Enter a number between 0 and 9, numbers with that digit won\'t be validate in the count:'))

#calls the process function
print(process(user_input, user_input_condition))