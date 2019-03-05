'''
classmates = ['Ros', 'Marcus', 'Flavio', 'Joseph', 'Maham', 'Vinay','Gungeet', 'Faris']

print(len(classmates)) 

print(classmates[0])

classmates.append('John')

classmates.insert(1,'Jane')

print(classmates[1])

print(classmates)

classmates.pop()

#print(classmates)

#print all elements in the list
#print(classmates)

#for c in classmates:
#    print(classmates[range(1,len(classmates)]))


#for name in classmates:
#    if name == 'Maham':
#        print('found in list')

#if 'Maham' in classmates:
#    print('Found Maham in list!!') 

#for idx, name in enumerate(classmates):
#    print(idx, name)    

lname = 'farrugia'

#print(lname[10:1])

print(lname[::-1])

x = ''
for r in range(len(lname),0,-1):
    x += lname[r-1]
    
print(x)
'''

disney_characters = ['simba','ariel','pumba','flounder','nala','ursula','scar','flotsam','timon']



for d in disney_characters:
    if 'u' in d:
        print('U are so unique')
    elif 'i' in d:
        print('I bet you\'re impressively intelligent')
    elif 'o' in d:
        print('O My! How Original!')
    else:
        print('a\'s and e\'s are so ordinary')



