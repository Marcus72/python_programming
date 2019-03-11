
'''
count = 0
while count < 10:
    print(count)
    count += 1

nums = ['2','84','6','8','10']
found = False 
key = 5 

while not found: 
    if key in nums:
        found = True
        break

for idx, item in enumerate(nums):
    if nums[idx] == key:
        break

my_nums = [1,3,15,8,7,6,5,-1]
for num in my_nums:
    if num % 2 == 0:
        continue
    print('{} is odd!'.format(num))
'''


#input a number

#loop while that number is not equal to your answer

#if input is smaller, print too small 

#print you got the number
'''
while answer != user_in:    
    if user_in > answer:
        print("Number {} is too big!".format(user_in)) 
    elif user_in < answer:
        print("Number {} is too small!".format(user_in))        
    else:
        print("Number {} is the number!".format(user_in))
        break
    user_in = int(input("Enter a number: "))

answer = 7
user_in = 8

while True:
    user_in = int(input('Enter a number: '))
    if user_in > answer:
        print('too big')
    if user_in < answer:
        print('too small')
    if user_in == answer:
        print('you got it')
        break

#find the sum of a list of numbers
ages = [25,39,45,41,27,18,33,65,11,50]
total_age = 0

for age in ages:    
    total_age += age

print('Total age is {}'.format(total_age))
'''

ages = [25,39,45,41,27,18,33,65,11,50]

