#Yining Hua
#CSC220
#A program that reads all the python files in a specified directory and prints out the number of lines of code in each (ignoring whitespace and comments)

import os

#Here's a short version.
'''
def main():

	#Note: This short version doesn't consider about the \''' multiline comment situation.

	path = input("Absolute path or your directory:  ")

	files = [filename for filename in os.listdir( path ) if filename.endswith( ".py" )]
	# files = {all the file names in path|end with .py} 
	
	for filename in files: 
		print(filename,sum(1 for line in open(path+"/"+filename) if line.strip() and not line.strip().startswith("#")))
        # Print(file name, sum of 1s|for (the the number of lines that are not empty or comments in the assigned file) times

'''

def main():
	#Note: This full version considers about the ''' multiline comment situation, uses functions and loops.

	abspath = input("Absolute path for the directory: ")
	readinType = '.py'
	files = Readdir(abspath,readinType)
	nlines = CountLines(abspath,files)

	for i in range (0,len(files)):
		print(files[i],nlines[i])
		i+=1


def Readdir(path,readinType):
	'''Read names of files in a given directory.
	'''
	return [filename for filename in os.listdir( path ) if filename.endswith( readinType )]


def CountLines(path,filenames):
	'''Count lines for each file in a given directory.
	'''  

	sumlist = []
	state = False
	#default state.

	for filename in filenames:

		nlines = 0
		f = open(os.path.join(path+"/"+filename))

		for line in f:
			state = isMulComment(line,state)
			#Consider\''' as a special case.
			if state == False:
				if line.strip() and not line.strip().startswith("'''") and not line.strip().startswith("#"):
					nlines += 1

		sumlist.append(nlines)

	return sumlist


def isMulComment(line, state):
	'''A state monitor for multiline comment(\''') circumstances
	'''
	
	if line.strip().startswith("'''") and state == False:
		if line.count("'''")%2==0:
		#Deal with the situation that 2 ''' appear in the same line.
			state = False
		else:
			state = True
			#if the multiline comment does not end in one line.

	elif line.strip().startswith("'''") or line.endswith("'''") and state == True:
	#when state is true and meets another ''', turn state to false.
		state = False

	return state


main()
