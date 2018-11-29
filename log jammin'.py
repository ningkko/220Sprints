#Yining Hua
#CSC220
#Sprint3
#Objective: write a @printdebugger decorator that logs the enter/exit of a function

#nextlevel1: also log the parameters passed into the function

#nextlevel2: indent to show functions that were called from within other functions

def printdebugger(func):
	'''Check if a function has been called'''

	def printdebugger_wrapper(*args,**kwargs):
		caller_name = inspect.stack[4]
		if calle_rname:
			indent+=1
		print("Entering function "+func.__name__)
		print(*args)
		print(**kwargs)
		function=func(*args,**kwargs)
		print("Exiting function "+func.__name__）
	    return function
	return printdebugger_wrapper

@printdebugger
def adder(a,b):
	c = a+b
	d = inside(6,c)
	return d

@printdebugger
def indside(a,b):
	return a+b

def main():
	indent = 0
	S = adder(3+4)
	print("S")
main()
