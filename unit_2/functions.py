'''
def high_low(my_var):
    if my_var > 10:
        print('HIGH')
    else:
        print('LOW')

high_low(11)

def FizzBuzz():
    for num in range(1,102):
        if num % 15 == 0:        
        #if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)   

FizzBuzz()

def capitalize(my_name):
    #convert to upper case
    return my_name.upper()

print(capitalize('marcus'))

def add_two(num):
    total = num + 2
    return total

print(add_two(4))
'''

def cap_first_letter(sentence):
    sen = sentence.split(' ')
    return sen


print(cap_first_letter('this is a sentence'))
'''
for cfl in cap_first_letter('this is a sentence'):
    new_word = cfl[0].upper()+cfl[1:]
    new_sentence += new_word
print(new_sentence)
   ''' 





























