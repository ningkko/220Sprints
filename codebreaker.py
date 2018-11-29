#With Qiaqia Ji
#The difficulty of factoring large prime numbers is a primary component of many modern encryption systems
#Objective: given a list of integers, return the prime factorization for each (including “PRIME” if the number is prime)

#Examples 

#********************************************

#121 = 11 * 11

#37 = PRIME

#240 = 2 * 2 * 2 * 2 * 3 * 5

#********************************************


import multiprocessing as mp

def check_prime(n):
	return n > 1 and all(n % i for i in range(2, n))

def prime_factors(n):
	# If n is prime, return prime
	if check_prime(n)==True: 
		result = str(n) + ' = ' + 'PRIME'
	# If n is not prime, find prime factors
	else:
		original = n
		primfac = []
		d = 2
		while d*d <= n:
			while (n % d) == 0:
			    primfac.append(d)
			    n //= d
			d += 1
		if n > 1:
		    primfac.append(n)

		result = str(original) + ' = ' 
		for i in range (len(primfac)):
			result += str(primfac[i])
			if i != len(primfac)-1:
				result += ' * '
	return result

def main():
	pool = mp.Pool(processes = 4)
	list_of_num = input('Enter numbers for factorization: ')
	nums = [int(x) for x in list_of_num.split()]
	result = [pool.apply(prime_factors, args = (n,)) for n in nums]
	pool.close()
	pool.join()
	print('********************************************')
	for r in result:
		print(r)
	print('********************************************')

main()
