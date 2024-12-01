def parser(f):
	n, k = [ int(i) for i in f.readline().split() ]
	quantity = [ int(f.readline()) for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	# We may assume that 1 <= k <= len(quantity)
	assert(1 <= k and k <= len(quantity))

	return cert, (quantity, k,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("quantity = " + str(input[0]))
	print("k = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
