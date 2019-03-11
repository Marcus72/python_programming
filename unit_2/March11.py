sentence = input('Enter a sentence: ')
res = ''
last_idx = len(sentence)-1
while last_idx >= 0:
    res += sentence[last_idx]
    last_idx -= 1

print(res)
