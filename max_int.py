#input a number
#it it is positive you input again
#if it is less than zero or negative it stops
num_int = int(input("Input a number: "))

while num_int < 0:
    num_int = int(input("Input a number: "))
    
