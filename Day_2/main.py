# let use make a function that calculate number of minutes and seconds

# For defining a function we have to use def keyword


# calculation_of_seconds=24*60*60

# def number_of_days(number_day):
#     print(f"In {number_day} we have {number_day*calculation_of_seconds} seconds")
    

# By default input function return string so we have to explictly define the type we want

# user_input_data=int(input("Enter the number of days "))

# number_of_days(user_input_data)



# now improve it by taking input from  the user


# now use if/else condition for make more logical


# let us create a menu to chose user input



def welcome():
    print("welcome choose \n 1. For to convert days to hours \n 2. For to convert hours to minutes \n 3. For to convert minutes to seconds")



welcome()






user_chose=int(input("Enter your chose "))
hours=24
minutes=60
seconds=60     

def days_to_hours(nums):
    if(nums<0):
        print("wrong choose")
    else:    
        print(f"In {nums} we have {nums*hours} hours")

def hours_to_minutes(nums):
    if(nums<0):
        print("wrong choose")
    else:        
        print(f"In {nums} we have {nums*minutes} minutes")


def minutes_to_seconds(nums):
    if(nums<0):
        print("wrong choose")
    else:    
        print(f"In {nums} we have {nums*seconds} seconds")  

if(user_chose==1):
    new_day=int(input("Enter number of days "))
    days_to_hours(new_day)
elif(user_chose==2):
    new_minute=int(input("Enter number of hours "))
    hours_to_minutes(new_minute) 
elif(user_chose==3):
    new_seconds=int(input("Enter number of minutes "))
    minutes_to_seconds(new_seconds)
else:
    print("none")          



  
# now validate the user input