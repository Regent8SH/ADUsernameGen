#!/usr/bin/env python3

#Example:
#./ADUsernameGen.py -i original.txt -o generated.txt

#If additional naming standards are needed, they can easily be added in the "mangleNames" function
#Please note: provided names without spaces will be disregarded
#I'M LOOKING AT YOU BEYONCE...

import sys, getopt, re, os

def mangleNames(first, last):
	mangledList = []
	mangledList.append(first+last)
	mangledList.append(first+'.'+last)
	mangledList.append(first[0]+last)
	mangledList.append(first+last[0])
	if len(first) > 3 and len(last) > 3:
		mangledList.append(first[0:3]+last[0:3])
		mangledList.append(first[0]+last[0:3])
	currentLen = len(mangledList)
	c = 0
	while c < currentLen:
		plus1 = "{}1".format(mangledList[c].strip())
		mangledList.append(plus1)
		c += 1
	return mangledList

def createList(inputfile):
	with open(inputfile) as f:
		nameLines = f.readlines()
		for name in nameLines:
			name = name.strip()
		firstList = []
		lastList = []
		for name in nameLines:
			if ' ' in name:
				splitList = re.split(' +', name)
				firstList.append(splitList[0])
				lastList.append(splitList[-1])
			else:
				pass
		finalList = []
		if len(firstList) == len(lastList):
			i = 0
			while i < len(firstList):
				first = firstList[i]
				last = lastList[i]
				mangledList = mangleNames(first, last)
				for mangled in mangledList:
					finalList.append(mangled)
				i += 1
		else:
			print("Error in list generation, please review name list.")
			system.exit(0)

		return finalList

def writeFile(finalList, outputfile):
	if os.path.exists(outputfile):
		os.remove(outputfile)
	with open(outputfile, 'w') as w:
		for item in finalList:
			w.write(item.strip() + '\n')



def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('ADUsernameGen.py -i original.txt -o generated.txt')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ('-h', '--help'):
      	print('ADUsernameGen.py -i <inputfile> -o <outputfile>')
      	sys.exit(0)
      elif opt == "-i":
         inputfile = arg
      elif opt == "-o":
         outputfile = arg

   finalList = createList(inputfile)
   writeFile(finalList, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])