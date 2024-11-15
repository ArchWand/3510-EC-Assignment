def parser(f):
	n = int(f.readline())
	locations = [ tuple(int(i) for i in f.readline().split()) for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (locations,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("locations = " + str(input[0]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
