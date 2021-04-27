

def isPrime(n):
	if n < 2:
		return False
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		else:
			return True

def factors(n):
	facts = []
	while n > 1:
		if isPrime(int(n)):
			facts.append(int(n))
			n = 1
		else:
			for i in range(1, 12):
				if n % i == 0 and isPrime(int(i)):
					n //= i
					facts.append(i)
					break
	
	facts.sort()
	return facts
	
if __name__ == "__main__":
	num = int(input())
	print(factors(num))