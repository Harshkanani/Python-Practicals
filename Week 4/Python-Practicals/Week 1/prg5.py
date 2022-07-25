lines = []
print("Enter a sentence to see the stats of a sentence : ")
while(True):
    line = input()
    if(line == 'c' or line == 'C'):
        break
    else:
        lines.append(line)

words = ''.join(lines)
no_of_words = words.split(' ')
print(words)

print("Number of words : ", len(no_of_words))

print("Number of characters : ", len(words))

alphanumeric = 0
for i in words:
    if(i.isalpha()):
        alphanumeric = alphanumeric + 1       
    
print("Number of alphanumeric characters : ", (alphanumeric*100)/len(words),'%')
