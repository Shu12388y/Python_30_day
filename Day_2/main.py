# let use make a function that calculate number of minutes and seconds

# For defining a function we have to use def keyword


calculation_of_seconds=24*60*60

def number_of_days(number_day):
    print(f"In {number_day} we have {number_day*calculation_of_seconds} seconds")
    

# By default input function return string so we have to explictly define the type we want

user_input_data=int(input("Enter the number of days "))

number_of_days(user_input_data)



# now improve it by taking input from  the user


