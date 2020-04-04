#Open text file
file = open('inputFile.txt', 'r')

#Iterate through and split lines
for line in file:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

file.close()