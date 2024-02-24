import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please Type a number larger then 0!')
        quit()

else:
    print('please type a number next time.')
    quit()

random_number = 4(top_of_range)


r = random.randrange(11)
