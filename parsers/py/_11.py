def parser(f):
	n, l = [ int(i) for i in f.readline().split() ]
	B = [ int(f.readline()) for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (B, l,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("B = " + str(input[0]))
	print("l = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
