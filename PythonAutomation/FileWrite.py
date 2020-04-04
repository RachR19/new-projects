#Open txt file
file = open('inputFile.txt', 'r')

#Create new text file
PassFile = open('PassFile.txt', 'w')
FailFile = open('FailFile.txt', 'w')

for line in file:
    line_split = line.split()
    if line_split[2] == 'P':
        PassFile.write(line)
    else: 
        FailFile.write(line)

file.close()
PassFile.close()
FailFile.close()