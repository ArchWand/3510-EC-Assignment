def parser(f):
	n = int(f.readline())
	blocks1 = [ int(f.readline()) for _ in range(n) ]
	blocks2 = [ int(f.readline()) for _ in range(n) ]

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (blocks1, blocks2,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("blocks1 = " + str(input[0]))
	print("blocks2 = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
