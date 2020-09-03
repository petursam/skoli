#prompt the user to input a number
#it should print out the highest number that was put in
#if it is less than zero (negative) it stops
#1 put an integer as the maximum integer, starting with zero
#2 use a while loop to get the input prompt repeatadly until the input is negative
#3
num_int = int(input("Input a number: "))
max_int = 0
while num_int >= 0:
    max_int = max(num_int, max_int)
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)
