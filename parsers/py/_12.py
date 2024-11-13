def parser(f):
	n, m = [ int(i) for i in f.readline().split() ]
	E = [ [int(i) for i in f.readline().split()] for _ in range(m) ]

	for t in E:
		assert(len(t) == 2)
	assert(f.readline() == "\n")

	c = int(f.readline())
	cert = [ tuple(int(i) for i in f.readline().split()) for _ in range(c) ]
	for t in E:
		assert(len(t) == 2)
	assert(f.readline().strip() == "")

	return cert, (n, E,)

def verifier(cert, ans):
	return sorted(cert) == sorted(ans)

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
