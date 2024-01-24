
  #  print("how's you")
  #for loop
for num in [1,2,3,4,5,6]:
    print(num)
for x in range(7):
    print('hello world ')
#demonstrating step value in range in for loop
#in below 1 is reffrered to as intial ,
# 20 is the final value
# 3 is the step value
for y in range(1,20,3):
    print(y)

# for loop ina table format that dispays  their squires
print ('number \t square')
print('-----------------')
for numbers in range(1,11):
    sqr=numbers **2
    print(numbers , '\t' , sqr)

# loop for hours ,minutes ,seconds
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours,':',minutes,':',seconds)