def parser(f):
	n = int(f.readline())
	formulas = [ f.readline().strip() for _ in range(n) ]

	assert(f.readline() == "\n")

	m = int(f.readline())
	cert = set( f.readline().strip() for _ in range(m) )

	return cert, (formulas,)

def verifier(cert, ans):
	return ans in cert

def error(cert, input, ans):
	print("Input:")
	print("formulas = " + str(input[0]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
