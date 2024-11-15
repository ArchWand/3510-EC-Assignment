def parser(f):
	n = int(f.readline())
	packages = [ [int(i) for i in f.readline().split()] for _ in range(n) ]

	for l in packages:
		assert(len(l) == 2)
	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (packages,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("packages = " + str(input[0]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
