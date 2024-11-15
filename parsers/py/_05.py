def parser(f):
	n, m, maxTime = [ int(i) for i in f.readline().split() ]
	energies = [ int(f.readline()) for _ in range(n) ]
	edges = [ [int(i) for i in f.readline().split()] for _ in range(m) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (energies, edges, maxTime,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("energies = " + str(input[0]))
	print("edges = " + str(input[1]))
	print("maxTime = " + str(input[2]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
