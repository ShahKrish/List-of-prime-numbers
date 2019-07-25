print('We will display all of the prime numbers till a certain number that you choose')
user_input=int(input('Enter the number here:'))
x = 0

for counter_1 in range(2,user_input+1):
    for counter_2 in range(2,counter_1):
        if counter_1 % counter_2 == 0:
            x = x+1

    if x > 0:
        pass
    else:
        print(counter_1)
    x=0
