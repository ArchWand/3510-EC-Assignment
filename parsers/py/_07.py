def parser(f):
	n = int(f.readline())
	time = [ [int(i) for i in f.readline().split()] for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())

	return cert, (time,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("quantity = " + str(input[0]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
