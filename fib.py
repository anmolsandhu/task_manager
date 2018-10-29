




def find_fib(n):

	prev = 0
	curr = 1

	for i in range(n):
		res = prev + curr
		prev = curr 
		curr = res
		print res

lookup_table = {}
def fib_dynamic(n):
	global lookup_table
	if n < 2:
		 lookup_table[n] = n
		 return n
	else:
		if lookup_table.get(n, None) != None:
			return lookup_table[n]

		lookup_table[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
		return lookup_table[n]





print fib_dynamic(6)