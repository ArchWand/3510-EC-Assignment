def parser(f):
	n, m = [ int(i) for i in f.readline().split() ]
	E = [ [int(i) for i in f.readline().split()] for _ in range(m) ]

	assert(f.readline() == "\n")

	c = int(f.readline())
	cert = [ tuple(int(i) for i in f.readline().split()) for _ in range(c) ]

	return cert, (n, E,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("n = " + str(input[0]))
	print("E = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
