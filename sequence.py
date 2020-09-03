#prompt the user for a number n that will be the maximum number in the sequence
#the sequence will add the numbers n up to the maximum number
#the formula for the sequence is the sum of the last 3 numbers in the sequence, example 1,2,3,6,11,20,37...
#using a "for" formula to find the sum of the numbers
n = int(input("Enter the length of the sequence: "))

total = 0
for x in range(0,n+1):
    total = total + x
    print(total)
