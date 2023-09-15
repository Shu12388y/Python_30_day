# string is data type in python
phase="hello this is phase"

# to print it 
print(phase)

# concatenate the string
new__phase="now i have add new phase"
print(phase+new__phase)


# to convert the string to uppercase
print(phase.upper())

# to convert the string to lowercase
print(phase.lower())

# to check whether the string is in upper case
print(phase.isupper())

# to check whether the string is in lower case
print(phase.islower())


# to check the length
print(len(phase))

# to get the elements in a string
print(phase[0])  # it will give the first letter of the string

# to get the index position of the letter in string
print(phase.index("n"))


# to replace a string with another string
# replace("string that you want to replace","new string")
print(phase.replace("now","then"))