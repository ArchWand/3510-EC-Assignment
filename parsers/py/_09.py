def parser(f):
	n = int(f.readline())
	nums = [ int(f.readline()) for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (nums,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("nums = " + str(input[0]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
