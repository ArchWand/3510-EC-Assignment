def parser(f):
	n = int(f.readline())
	ticket = f.readline()

	assert(f.readline() == "\n")

	cert = bool(f.readline())

	return cert, (n, ticket,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("n = " + str(input[0]))
	print("ticket = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
