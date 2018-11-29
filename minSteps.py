#Yining Hua
#CSC220
#Sprint 3
#	Given a positive integer n, perform any one of the
#	following 3 steps: 
#	1.Subtract 1.
#	2.If n is divisible by 2, divide by 2. 
#	3.If n is divisible by 3, divide by 3. 
#	Compute the minimum number of steps that takes n to 1.
def main():

	num = 60
	known_result=[]
	for i in range(num+1):
		known_result.append(0)
		i+=1
	divisors = [2,3]

	print(minSteps(divisors,num,known_result))


def minSteps(divisors,num,known_result):
	for value in range (1,num+1):
		steps = value-1#base case: getting every number to 1 by substracting 1s
		for divisor in [divisors for divisors in divisors if divisors<=value]:
			if not value%divisor: #step 2 & 3: devide.
				steps = min(known_result[value//divisor]+1,steps)#return the samller value
			elif not (value-1)%divisor: #step 1: substract 1.
				steps = min(known_result[(value-1)//divisor]+2,steps)
		known_result[value]=steps #refresh stored step value for that number

	return known_result[num]#return the step number stored in the NUMth number.


main()
