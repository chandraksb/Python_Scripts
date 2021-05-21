# Python Bubble sort algorithm
# Takes file as input. First sorts each line within and then each line of the file
# 

# Open the input and output files
FH = open("sort_input.txt", 'r')
FH_NEW = open("sort_output.txt", 'w')

i=1
linesDict = {}  #Temp Dictionary 

#Read the contents to a Temp Dictionary
for line in FH:
	linesDict[i] = list(line.split())
	i += 1

def sort_lines_nfiles():
	v=[]  #Temp List
	i=1

	# With-in line bobble sorting
	for v in linesDict.values():
		sizeList = len(v)
		
		for x in range(sizeList-1):
			for y in range(0,sizeList-x-1):
				if v[y] > v[y+1]:
					v[y], v[y+1] = v[y+1], v[y]  
		i += 1
		
	# Lines bobble sorting
	tempListVal = list(linesDict.values())
	#print(f"Dict List is : {tempListVal}")
	
	sizeDict = len(tempListVal)
	for x in range(sizeDict-1):
		for y in range(0,sizeDict-x-1):
			if tempListVal[y] > tempListVal[y+1]:
				tempListVal[y], tempListVal[y+1] = tempListVal[y+1], tempListVal[y]

	# Write the sorted output to a new file
	for line in tempListVal:
		tmpStr1 = ' '.join(map(str, line)) + '\n'
		FH_NEW.write(str(tmpStr1))

	print("New file sort_output.txt file is ready with bubble sorted")

# Close the opened files
FH_NEW.close()
FH.close()
#END of sort_lines_nfiles() function


sort_lines_nfiles()